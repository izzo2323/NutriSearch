"use client";
import { useState, useEffect, useMemo } from "react";
import { useSearchParams } from "next/navigation";
import { useQuery, useMutation } from "@tanstack/react-query";
import { Loader2, Trash2, UtensilsCrossed, ChevronDown, ChevronUp } from "lucide-react";
import {
  BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, Cell
} from "recharts";
import { api } from "@/lib/api";
import type { MenuItem, SortOption } from "@/lib/types";
import type { BuiltMealGroup } from "@/components/IngredientBuilder";
import MenuItemCard from "@/components/MenuItemCard";

const MACRO_COLORS: Record<string, string> = {
  Protein: "#22c55e", Carbs: "#f59e0b", Fat: "#ef4444",
};

// ── Entry types ───────────────────────────────────────────────────────────────
type SingleEntry = { type: "item";  item: MenuItem; quantity: number };
type GroupEntry  = { type: "built"; label: string; icon: string; items: MenuItem[]; expanded: boolean };
type MealEntry   = SingleEntry | GroupEntry;

function allItems(entries: MealEntry[]): { menu_item_id: number; quantity: number }[] {
  const out: { menu_item_id: number; quantity: number }[] = [];
  for (const e of entries) {
    if (e.type === "item")  out.push({ menu_item_id: e.item.id, quantity: e.quantity });
    else e.items.forEach((i) => out.push({ menu_item_id: i.id, quantity: 1 }));
  }
  return out;
}

function resolveActiveChain(entries: MealEntry[]) {
  if (!entries.length) return null;
  const firstChain = entries[0].type === "item"
    ? entries[0].item.chain
    : entries[0].items[0]?.chain;
  if (!firstChain) return null;
  const allSame = entries.every((e) => {
    const c = e.type === "item" ? e.item.chain : e.items[0]?.chain;
    return c?.id === firstChain.id;
  });
  return allSame ? firstChain : null;
}

// ─────────────────────────────────────────────────────────────────────────────

export default function MealBuilderPage() {
  const searchParams = useSearchParams();
  const [entries,     setEntries]     = useState<MealEntry[]>([]);
  const [searchQ,     setSearchQ]     = useState("");
  const [searchChain, setSearchChain] = useState<number | undefined>();
  const [sort] = useState<SortOption>("healthiest");

  const { data: chains = [] } = useQuery({
    queryKey: ["chains-list"],
    queryFn:  () => api.chains.list(),
    staleTime: 300_000,
  });

  // ── Load from URL params (individual items) + sessionStorage (groups) ────
  useEffect(() => {
    const idsParam  = searchParams.get("items");
    const groupsRaw = sessionStorage.getItem("mealGroups");
    sessionStorage.removeItem("mealGroups");   // consume once

    const loadIndividual = idsParam
      ? Promise.all(
          idsParam.split(",").map(Number).filter(Boolean).map((id) => api.menu.get(id))
        ).then((items): SingleEntry[] =>
          items.map((item) => ({ type: "item" as const, item, quantity: 1 }))
        )
      : Promise.resolve([] as SingleEntry[]);

    const loadGroups = groupsRaw
      ? Promise.all(
          (JSON.parse(groupsRaw) as BuiltMealGroup[]).map((g) =>
            Promise.all(g.itemIds.map((id) => api.menu.get(id))).then(
              (items): GroupEntry => ({
                type: "built", label: g.label, icon: g.icon, items, expanded: false,
              })
            )
          )
        )
      : Promise.resolve([] as GroupEntry[]);

    Promise.all([loadIndividual, loadGroups]).then(([singles, groups]) => {
      const merged: MealEntry[] = [...singles, ...groups];
      if (!merged.length) return;
      setEntries(merged);
      const firstChain =
        singles[0]?.item.chain?.id ??
        groups[0]?.items[0]?.chain?.id;
      if (firstChain) setSearchChain(firstChain);
    });
  }, [searchParams]);

  // ── Search ───────────────────────────────────────────────────────────────
  const { data: searchResults = [], isFetching } = useQuery({
    queryKey: ["meal-search", searchQ, searchChain, sort],
    queryFn: () => api.menu.list({
      q: searchQ || undefined, chain_id: searchChain, sort, limit: 30,
    }),
    enabled: searchQ.length > 1 || !!searchChain,
    staleTime: 30_000,
  });

  // ── Mutation ─────────────────────────────────────────────────────────────
  const analyzeMutation = useMutation({
    mutationFn: () => api.meal.analyze(allItems(entries)),
  });

  // ── Entry management ──────────────────────────────────────────────────────
  const addItem = (item: MenuItem) => {
    setEntries((prev) => {
      const existing = prev.find((e) => e.type === "item" && e.item.id === item.id);
      if (existing && existing.type === "item") {
        return prev.map((e) =>
          e.type === "item" && e.item.id === item.id ? { ...e, quantity: e.quantity + 1 } : e
        );
      }
      return [...prev, { type: "item", item, quantity: 1 }];
    });
  };

  const removeEntry = (idx: number) => setEntries((p) => p.filter((_, i) => i !== idx));

  const updateQty = (idx: number, qty: number) => {
    if (qty < 1) { removeEntry(idx); return; }
    setEntries((p) =>
      p.map((e, i) => i === idx && e.type === "item" ? { ...e, quantity: qty } : e)
    );
  };

  const toggleExpand = (idx: number) =>
    setEntries((p) =>
      p.map((e, i) => i === idx && e.type === "built" ? { ...e, expanded: !e.expanded } : e)
    );

  // ── Derived ───────────────────────────────────────────────────────────────
  const activeChain = useMemo(() => resolveActiveChain(entries), [entries]);
  const analysis    = analyzeMutation.data;

  const mealLabel = useMemo(() => {
    if (!entries.length) return "Meal Builder";
    if (activeChain)     return `Building ${activeChain.name} Meal`;
    return "Building Custom Meal";
  }, [entries, activeChain]);

  const mealSubLabel = useMemo(() => {
    if (!entries.length) return "Add items from any restaurant to see your nutrition breakdown.";
    if (activeChain)     return activeChain.cuisine_type ?? activeChain.name;
    const names = [...new Set(
      entries.map((e) =>
        e.type === "item" ? e.item.chain?.name : e.items[0]?.chain?.name
      ).filter(Boolean)
    )];
    return `Items from ${names.join(", ")}`;
  }, [entries, activeChain]);

  const macroData = analysis ? [
    { name: "Protein", value: Math.round(analysis.totals.protein_g)    },
    { name: "Carbs",   value: Math.round(analysis.totals.total_carbs_g) },
    { name: "Fat",     value: Math.round(analysis.totals.total_fat_g)   },
  ] : [];

  // ── Render ────────────────────────────────────────────────────────────────
  return (
    <div className="max-w-6xl mx-auto px-4 py-8">
      {/* Header */}
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 flex items-center gap-3">
          {activeChain && (
            <span className="w-10 h-10 rounded-full bg-brand-100 text-brand-700 flex items-center justify-center font-black text-lg">
              {activeChain.name.charAt(0)}
            </span>
          )}
          {mealLabel}
        </h1>
        <p className="text-gray-500 mt-1">{mealSubLabel}</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">

        {/* ── Left: search ────────────────────────────────────────────── */}
        <div>
          <h2 className="font-semibold text-lg mb-3">Add Items</h2>
          <div className="flex gap-2 mb-3">
            <select
              value={searchChain ?? ""}
              onChange={(e) => setSearchChain(e.target.value ? Number(e.target.value) : undefined)}
              className="border rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-brand-500"
            >
              <option value="">All restaurants</option>
              {chains.map((c) => <option key={c.id} value={c.id}>{c.name}</option>)}
            </select>
            <input
              type="text" placeholder="Search menu items…" value={searchQ}
              onChange={(e) => setSearchQ(e.target.value)}
              className="flex-1 border rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-brand-500"
            />
          </div>
          {isFetching && <div className="flex justify-center py-4"><Loader2 className="w-5 h-5 animate-spin text-brand-600" /></div>}
          <div className="grid gap-2 max-h-[600px] overflow-y-auto pr-1">
            {searchResults.map((item) => <MenuItemCard key={item.id} item={item} onAddToMeal={addItem} />)}
            {!isFetching && (searchQ.length > 1 || searchChain) && !searchResults.length && (
              <p className="text-center text-gray-400 py-6">No items found.</p>
            )}
            {!searchQ && !searchChain && (
              <p className="text-gray-400 text-sm text-center py-8">
                Type a food name or select a restaurant to search items.
              </p>
            )}
          </div>
        </div>

        {/* ── Right: meal tray ────────────────────────────────────────── */}
        <div>
          <div className="flex items-center justify-between mb-3">
            <h2 className="font-semibold text-lg">
              {entries.length === 0 ? "Your Meal" : mealLabel}
            </h2>
            {entries.length > 0 && (
              <button
                onClick={() => { setEntries([]); analyzeMutation.reset(); }}
                className="text-xs text-gray-400 hover:text-red-500 flex items-center gap-1"
              >
                <UtensilsCrossed className="w-3.5 h-3.5" /> Clear all
              </button>
            )}
          </div>

          {entries.length === 0 ? (
            <div className="bg-gray-50 border-2 border-dashed border-gray-200 rounded-xl p-8 text-center text-gray-400">
              Add items from the left, or build a meal from a restaurant's ingredient selector.
            </div>
          ) : (
            <>
              {/* Chain badge */}
              {activeChain && (
                <div className="flex items-center gap-2 bg-brand-50 border border-brand-200 rounded-lg px-3 py-2 mb-3">
                  <span className="w-6 h-6 rounded-full bg-brand-600 text-white flex items-center justify-center text-xs font-bold">
                    {activeChain.name.charAt(0)}
                  </span>
                  <span className="text-sm font-medium text-brand-800">{activeChain.name}</span>
                  {activeChain.cuisine_type && (
                    <span className="text-xs text-brand-600 ml-auto">{activeChain.cuisine_type}</span>
                  )}
                </div>
              )}

              <div className="space-y-2 mb-4">
                {entries.map((entry, idx) => {

                  /* ── Built meal group ───────────────────────────────────── */
                  if (entry.type === "built") {
                    const groupCal = entry.items.reduce(
                      (s, i) => s + (Number(i.nutrition?.calories) || 0), 0
                    );
                    return (
                      <div key={idx} className="bg-white border border-brand-200 rounded-xl overflow-hidden">
                        {/* Group header */}
                        <div className="flex items-center justify-between px-3 py-2.5 bg-brand-50">
                          <div className="flex items-center gap-2 flex-1 min-w-0">
                            <span className="text-xl">{entry.icon}</span>
                            <div className="min-w-0">
                              <p className="font-semibold text-sm text-gray-900">{entry.label}</p>
                              {!entry.expanded && (
                                <p className="text-xs text-gray-500 truncate">
                                  {entry.items.map((i) => i.name).join(" · ")}
                                </p>
                              )}
                            </div>
                          </div>
                          <div className="flex items-center gap-2 ml-2 shrink-0">
                            <span className="text-sm font-semibold text-brand-700">{groupCal} cal</span>
                            <button
                              onClick={() => toggleExpand(idx)}
                              className="text-gray-400 hover:text-gray-600 p-1"
                              title={entry.expanded ? "Collapse" : "Show ingredients"}
                            >
                              {entry.expanded
                                ? <ChevronUp className="w-4 h-4" />
                                : <ChevronDown className="w-4 h-4" />
                              }
                            </button>
                            <button onClick={() => removeEntry(idx)} className="text-red-400 hover:text-red-600 p-1">
                              <Trash2 className="w-4 h-4" />
                            </button>
                          </div>
                        </div>

                        {/* Expanded ingredient list */}
                        {entry.expanded && (
                          <div className="divide-y divide-gray-50">
                            {entry.items.map((item, ii) => (
                              <div key={ii} className="flex justify-between items-center px-4 py-1.5 text-sm">
                                <span className="text-gray-700">{item.name}</span>
                                <span className="text-gray-400 text-xs">
                                  {item.nutrition?.calories != null ? `${item.nutrition.calories} cal` : "—"}
                                </span>
                              </div>
                            ))}
                          </div>
                        )}
                      </div>
                    );
                  }

                  /* ── Single item ─────────────────────────────────────────── */
                  return (
                    <div key={idx} className="flex items-center justify-between bg-white border rounded-lg px-3 py-2">
                      <div className="flex-1 min-w-0">
                        <p className="text-sm font-medium truncate">{entry.item.name}</p>
                        {!activeChain && (
                          <p className="text-xs text-gray-400">{entry.item.chain?.name}</p>
                        )}
                        {entry.item.nutrition?.calories != null && (
                          <p className="text-xs text-gray-400">
                            {entry.item.nutrition.calories} cal
                            {entry.quantity > 1 && ` × ${entry.quantity} = ${entry.item.nutrition.calories * entry.quantity} cal`}
                          </p>
                        )}
                      </div>
                      <div className="flex items-center gap-2 ml-2">
                        <button onClick={() => updateQty(idx, entry.quantity - 1)}
                                className="w-6 h-6 rounded border flex items-center justify-center text-gray-500 hover:bg-gray-100">−</button>
                        <span className="text-sm w-4 text-center">{entry.quantity}</span>
                        <button onClick={() => updateQty(idx, entry.quantity + 1)}
                                className="w-6 h-6 rounded border flex items-center justify-center text-gray-500 hover:bg-gray-100">+</button>
                        <button onClick={() => removeEntry(idx)} className="text-red-400 hover:text-red-600 ml-1">
                          <Trash2 className="w-4 h-4" />
                        </button>
                      </div>
                    </div>
                  );
                })}
              </div>

              <button
                onClick={() => analyzeMutation.mutate()}
                disabled={analyzeMutation.isPending}
                className="w-full bg-brand-600 text-white py-2 rounded-lg hover:bg-brand-700 font-medium flex items-center justify-center gap-2 disabled:opacity-60"
              >
                {analyzeMutation.isPending && <Loader2 className="w-4 h-4 animate-spin" />}
                Analyze Nutrition
              </button>
            </>
          )}

          {/* Analysis results */}
          {analysis && (
            <div className="mt-6 space-y-6">
              <div className="bg-white border rounded-xl p-4 text-center">
                <p className="text-gray-500 text-sm">
                  {activeChain ? `${activeChain.name} Meal` : "Meal"} · Total Calories
                </p>
                <p className="text-5xl font-black text-gray-900">{analysis.totals.calories}</p>
                <p className="text-sm text-gray-400 mt-1">
                  {analysis.daily_pct.calories}% of 2,000 cal daily value
                </p>
              </div>

              <div className="bg-white border rounded-xl p-4">
                <h3 className="font-semibold mb-3">Macros (grams)</h3>
                <ResponsiveContainer width="100%" height={160}>
                  <BarChart data={macroData} barCategoryGap="30%">
                    <XAxis dataKey="name" tick={{ fontSize: 12 }} />
                    <YAxis tick={{ fontSize: 12 }} />
                    <Tooltip formatter={(v) => [`${v}g`]} />
                    <Bar dataKey="value" radius={[4, 4, 0, 0]}>
                      {macroData.map((entry) => (
                        <Cell key={entry.name} fill={MACRO_COLORS[entry.name]} />
                      ))}
                    </Bar>
                  </BarChart>
                </ResponsiveContainer>
              </div>

              <div className="bg-white border rounded-xl p-4">
                <h3 className="font-semibold mb-3">% Daily Value (2,000 cal diet)</h3>
                <div className="space-y-2">
                  {(
                    [
                      ["Total Fat",     analysis.daily_pct.total_fat],
                      ["Saturated Fat", analysis.daily_pct.saturated_fat],
                      ["Cholesterol",   analysis.daily_pct.cholesterol],
                      ["Sodium",        analysis.daily_pct.sodium],
                      ["Total Carbs",   analysis.daily_pct.total_carbs],
                      ["Dietary Fiber", analysis.daily_pct.dietary_fiber],
                      ["Protein",       analysis.daily_pct.protein],
                    ] as [string, number][]
                  ).map(([label, pct]) => (
                    <div key={label}>
                      <div className="flex justify-between text-xs mb-0.5">
                        <span>{label}</span>
                        <span className={pct > 100 ? "text-red-600 font-bold" : "text-gray-600"}>{pct}%</span>
                      </div>
                      <div className="h-2 bg-gray-100 rounded-full overflow-hidden">
                        <div
                          className={`h-full rounded-full ${pct > 100 ? "bg-red-500" : pct > 75 ? "bg-yellow-500" : "bg-brand-500"}`}
                          style={{ width: `${Math.min(pct, 100)}%` }}
                        />
                      </div>
                    </div>
                  ))}
                </div>
              </div>

              <div className="bg-white border rounded-xl p-4">
                <h3 className="font-semibold mb-3">Full Breakdown</h3>
                <div className="grid grid-cols-2 gap-x-6 gap-y-1 text-sm">
                  {(
                    [
                      ["Calories",      analysis.totals.calories,        ""],
                      ["Total Fat",     analysis.totals.total_fat_g,     "g"],
                      ["Saturated Fat", analysis.totals.saturated_fat_g, "g"],
                      ["Trans Fat",     analysis.totals.trans_fat_g,     "g"],
                      ["Cholesterol",   analysis.totals.cholesterol_mg,  "mg"],
                      ["Sodium",        analysis.totals.sodium_mg,       "mg"],
                      ["Total Carbs",   analysis.totals.total_carbs_g,   "g"],
                      ["Dietary Fiber", analysis.totals.dietary_fiber_g, "g"],
                      ["Total Sugars",  analysis.totals.total_sugars_g,  "g"],
                      ["Protein",       analysis.totals.protein_g,       "g"],
                    ] as [string, number, string][]
                  ).map(([label, val, unit]) => (
                    <div key={label} className="flex justify-between py-0.5 border-b border-gray-50">
                      <span className="text-gray-600">{label}</span>
                      <span className="font-medium">
                        {typeof val === "number" ? val.toFixed(unit === "" ? 0 : 1) : val}{unit}
                      </span>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
