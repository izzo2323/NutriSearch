"use client";
import { useState, useMemo } from "react";
import { useParams, useRouter } from "next/navigation";
import { useQuery } from "@tanstack/react-query";
import { ArrowLeft, ShoppingCart, Utensils, Loader2 } from "lucide-react";
import Link from "next/link";
import { api } from "@/lib/api";
import type { MenuItem } from "@/lib/types";
import NutritionFacts from "@/components/NutritionFacts";
import CalorieBadge from "@/components/CalorieBadge";

// Category names that count as "sides" or "drinks" across all chains
const SIDE_KEYWORDS  = ["side", "fries", "salad", "soup", "tots", "ring", "bread"];
const DRINK_KEYWORDS = ["drink", "beverage", "shake", "frosty", "milkshake", "smoothie",
                        "coffee", "tea", "lemonade", "limeade", "cold brew", "blast",
                        "frappuccino", "juice"];

function matchesAny(name: string, keywords: string[]) {
  const lower = name.toLowerCase();
  return keywords.some((k) => lower.includes(k));
}

function safeNum(v: number | string | null | undefined): number {
  return v == null ? 0 : Number(v);
}

interface MealTotals {
  calories: number;
  protein:  number;
  carbs:    number;
  fat:      number;
  sugar:    number;
  sodium:   number;
}

function addTotals(acc: MealTotals, item: MenuItem, qty = 1): MealTotals {
  const n = item.nutrition;
  if (!n) return acc;
  return {
    calories: acc.calories + safeNum(n.calories)        * qty,
    protein:  acc.protein  + safeNum(n.protein_g)       * qty,
    carbs:    acc.carbs    + safeNum(n.total_carbs_g)   * qty,
    fat:      acc.fat      + safeNum(n.total_fat_g)     * qty,
    sugar:    acc.sugar    + safeNum(n.total_sugars_g)  * qty,
    sodium:   acc.sodium   + safeNum(n.sodium_mg)       * qty,
  };
}

const ZERO: MealTotals = { calories: 0, protein: 0, carbs: 0, fat: 0, sugar: 0, sodium: 0 };

// ─────────────────────────────────────────────────────────────────────────────

export default function MenuItemDetailPage() {
  const { id } = useParams<{ id: string }>();
  const router  = useRouter();
  const itemId  = Number(id);

  const [selectedSideId,  setSideId]  = useState<number | null>(null);
  const [selectedDrinkId, setDrinkId] = useState<number | null>(null);

  // Fetch the main item
  const { data: item, isLoading } = useQuery({
    queryKey: ["menu-item", itemId],
    queryFn:  () => api.menu.get(itemId),
  });

  const chainId = item?.chain?.id;

  // Fetch all items for this chain (for the side/drink selectors)
  const { data: chainItems = [] } = useQuery({
    queryKey: ["chain-all-items", chainId],
    queryFn:  () => api.menu.list({ chain_id: chainId, limit: 300 }),
    enabled:  !!chainId,
    staleTime: 300_000,
  });

  // Fetch preset meals that include this item (for "part of these combos")
  const { data: presets = [] } = useQuery({
    queryKey: ["presets", chainId],
    queryFn:  () => api.presets.list(chainId),
    enabled:  !!chainId,
    staleTime: 300_000,
  });

  const relatedPresets = useMemo(
    () => presets.filter((p) => p.items.some((pi) => pi.menu_item.id === itemId)),
    [presets, itemId]
  );

  // Buckets for dropdowns
  const sides = useMemo(
    () => chainItems.filter((i) => i.id !== itemId && matchesAny(i.category?.name ?? "", SIDE_KEYWORDS)),
    [chainItems, itemId]
  );
  const drinks = useMemo(
    () => chainItems.filter((i) => i.id !== itemId && matchesAny(i.category?.name ?? "", DRINK_KEYWORDS)),
    [chainItems, itemId]
  );

  const selectedSide  = sides.find((i)  => i.id === selectedSideId)  ?? null;
  const selectedDrink = drinks.find((i) => i.id === selectedDrinkId) ?? null;

  // Live meal total
  const totals = useMemo(() => {
    let t = ZERO;
    if (item)         t = addTotals(t, item);
    if (selectedSide) t = addTotals(t, selectedSide);
    if (selectedDrink) t = addTotals(t, selectedDrink);
    return t;
  }, [item, selectedSide, selectedDrink]);

  const mealIsCustomised = selectedSide || selectedDrink;

  const goToMealBuilder = () => {
    const ids = [
      item?.id,
      selectedSide?.id,
      selectedDrink?.id,
    ].filter(Boolean).join(",");
    router.push(`/meal-builder?items=${ids}`);
  };

  if (isLoading || !item) {
    return (
      <div className="flex justify-center items-center min-h-[40vh]">
        <Loader2 className="w-8 h-8 animate-spin text-brand-600" />
      </div>
    );
  }

  return (
    <div className="max-w-5xl mx-auto px-4 py-8">
      {/* Back */}
      <Link
        href={`/restaurants/${chainId}`}
        className="inline-flex items-center gap-1 text-sm text-brand-600 hover:underline mb-6"
      >
        <ArrowLeft className="w-4 h-4" />
        Back to {item.chain?.name}
      </Link>

      {/* Title */}
      <div className="mb-8">
        <div className="flex items-start gap-3 flex-wrap">
          <h1 className="text-3xl font-bold text-gray-900 flex-1">{item.name}</h1>
          <CalorieBadge calories={item.nutrition?.calories ?? null} />
        </div>
        <p className="text-gray-500 mt-1 text-sm">
          {item.chain?.name}
          {item.category && <> · {item.category.name}</>}
          {item.serving_size && <> · {item.serving_size}</>}
        </p>
        {item.description && (
          <p className="text-gray-600 mt-2">{item.description}</p>
        )}
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-8 items-start">

        {/* ── Left: Nutrition Facts ───────────────────────────────── */}
        <div>
          {item.nutrition
            ? <NutritionFacts n={item.nutrition} servingSize={item.serving_size} />
            : <p className="text-gray-400 text-sm">No nutrition data available.</p>
          }
        </div>

        {/* ── Right: Build Your Meal ──────────────────────────────── */}
        <div className="bg-white border border-gray-200 rounded-2xl p-6 space-y-5">
          <h2 className="font-bold text-lg flex items-center gap-2">
            <Utensils className="w-5 h-5 text-brand-600" />
            Build Your Meal
          </h2>

          {/* Base item */}
          <div className="bg-brand-50 border border-brand-200 rounded-lg px-4 py-3 flex justify-between items-center">
            <div>
              <p className="font-semibold text-sm text-gray-900">{item.name}</p>
              <p className="text-xs text-gray-500 mt-0.5">Base item</p>
            </div>
            <span className="text-sm font-bold text-brand-700">
              {item.nutrition?.calories ?? "—"} cal
            </span>
          </div>

          {/* Side selector */}
          {sides.length > 0 && (
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1.5">
                Add a Side
              </label>
              <div className="relative">
                <select
                  value={selectedSideId ?? ""}
                  onChange={(e) => setSideId(e.target.value ? Number(e.target.value) : null)}
                  className="w-full border border-gray-300 rounded-lg px-3 py-2.5 text-sm appearance-none bg-white focus:outline-none focus:ring-2 focus:ring-brand-500 pr-8"
                >
                  <option value="">No side</option>
                  {sides.map((s) => (
                    <option key={s.id} value={s.id}>
                      {s.name}{s.nutrition?.calories != null ? ` — ${s.nutrition.calories} cal` : ""}
                    </option>
                  ))}
                </select>
                <span className="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 text-xs">▼</span>
              </div>
              {selectedSide && (
                <div className="mt-1.5 flex gap-3 text-xs text-gray-500 pl-1">
                  {selectedSide.nutrition?.protein_g      != null && <span>{selectedSide.nutrition.protein_g}g protein</span>}
                  {selectedSide.nutrition?.total_carbs_g  != null && <span>{selectedSide.nutrition.total_carbs_g}g carbs</span>}
                  {selectedSide.nutrition?.total_fat_g    != null && <span>{selectedSide.nutrition.total_fat_g}g fat</span>}
                  {selectedSide.nutrition?.total_sugars_g != null && <span>{selectedSide.nutrition.total_sugars_g}g sugar</span>}
                </div>
              )}
            </div>
          )}

          {/* Drink selector */}
          {drinks.length > 0 && (
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1.5">
                Add a Drink
              </label>
              <div className="relative">
                <select
                  value={selectedDrinkId ?? ""}
                  onChange={(e) => setDrinkId(e.target.value ? Number(e.target.value) : null)}
                  className="w-full border border-gray-300 rounded-lg px-3 py-2.5 text-sm appearance-none bg-white focus:outline-none focus:ring-2 focus:ring-brand-500 pr-8"
                >
                  <option value="">No drink</option>
                  {drinks.map((d) => (
                    <option key={d.id} value={d.id}>
                      {d.name}{d.nutrition?.calories != null ? ` — ${d.nutrition.calories} cal` : ""}
                    </option>
                  ))}
                </select>
                <span className="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 text-xs">▼</span>
              </div>
              {selectedDrink && (
                <div className="mt-1.5 flex gap-3 text-xs text-gray-500 pl-1">
                  {selectedDrink.nutrition?.total_sugars_g != null && <span>{selectedDrink.nutrition.total_sugars_g}g sugar</span>}
                  {selectedDrink.nutrition?.sodium_mg != null && <span>{selectedDrink.nutrition.sodium_mg}mg sodium</span>}
                </div>
              )}
            </div>
          )}

          {/* Running total */}
          <div className={`rounded-xl p-4 border ${mealIsCustomised ? "bg-gray-900 border-gray-800 text-white" : "bg-gray-50 border-gray-200 text-gray-800"}`}>
            <div className="flex justify-between items-baseline mb-3">
              <span className={`text-sm font-medium ${mealIsCustomised ? "text-gray-300" : "text-gray-500"}`}>
                {mealIsCustomised ? "Meal Total" : "Item Total"}
              </span>
              <span className="text-3xl font-black">
                {Math.round(totals.calories)} <span className="text-lg font-normal">cal</span>
              </span>
            </div>
            <div className="grid grid-cols-2 gap-x-4 gap-y-1.5 text-sm">
              {[
                ["Protein",  `${totals.protein.toFixed(1)}g`],
                ["Carbs",    `${totals.carbs.toFixed(1)}g`],
                ["Fat",      `${totals.fat.toFixed(1)}g`],
                ["Sugar",    `${totals.sugar.toFixed(1)}g`],
                ["Sodium",   `${Math.round(totals.sodium)}mg`],
              ].map(([label, val]) => (
                <div key={label} className="flex justify-between">
                  <span className={mealIsCustomised ? "text-gray-400" : "text-gray-500"}>{label}</span>
                  <span className="font-semibold">{val}</span>
                </div>
              ))}
            </div>
          </div>

          {/* Action buttons */}
          <div className="flex flex-col gap-2">
            <button
              onClick={goToMealBuilder}
              className="w-full flex items-center justify-center gap-2 bg-brand-600 text-white font-semibold py-3 rounded-xl hover:bg-brand-700 transition-colors"
            >
              <ShoppingCart className="w-4 h-4" />
              {mealIsCustomised ? "Add Meal to Builder" : "Add to Meal Builder"}
            </button>
            {mealIsCustomised && (
              <button
                onClick={() => { setSideId(null); setDrinkId(null); }}
                className="w-full text-sm text-gray-500 hover:text-gray-700 py-1"
              >
                Clear customizations
              </button>
            )}
          </div>
        </div>
      </div>

      {/* Related preset combos */}
      {relatedPresets.length > 0 && (
        <div className="mt-10">
          <h2 className="font-semibold text-lg text-gray-900 mb-3">
            Popular Combos That Include This Item
          </h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {relatedPresets.map((preset) => {
              const cal = preset.totals?.calories ?? 0;
              const calCls = cal < 600 ? "text-green-700 bg-green-50" : cal < 1000 ? "text-yellow-700 bg-yellow-50" : "text-red-700 bg-red-50";
              return (
                <div key={preset.id} className="bg-white border border-gray-200 rounded-xl p-4 space-y-2">
                  <div className="flex justify-between items-start gap-2">
                    <p className="font-semibold text-sm text-gray-900">{preset.name}</p>
                    <span className={`text-xs font-bold px-2 py-0.5 rounded-full whitespace-nowrap ${calCls}`}>
                      {cal} cal
                    </span>
                  </div>
                  <ul className="text-xs text-gray-500 space-y-0.5">
                    {preset.items.map((pi, i) => (
                      <li key={i}>
                        {pi.quantity > 1 && <b>×{pi.quantity} </b>}
                        {pi.menu_item.name}
                      </li>
                    ))}
                  </ul>
                  <button
                    onClick={() => {
                      const ids = preset.items
                        .flatMap((pi) => Array(pi.quantity).fill(pi.menu_item.id))
                        .join(",");
                      router.push(`/meal-builder?items=${ids}`);
                    }}
                    className="w-full text-xs bg-brand-600 text-white py-1.5 rounded-lg hover:bg-brand-700 mt-1"
                  >
                    Open in Meal Builder
                  </button>
                </div>
              );
            })}
          </div>
        </div>
      )}
    </div>
  );
}
