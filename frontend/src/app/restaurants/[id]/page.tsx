"use client";
import { useState } from "react";
import { useQuery } from "@tanstack/react-query";
import { Loader2, ShoppingCart, MapPin } from "lucide-react";
import { useParams, useRouter } from "next/navigation";
import Link from "next/link";
import { api } from "@/lib/api";
import type { MenuItem, SortOption, PresetMeal } from "@/lib/types";
import MenuItemCard from "@/components/MenuItemCard";
import PresetMealCard from "@/components/PresetMealCard";
import IngredientBuilder, { type BuiltMealGroup } from "@/components/IngredientBuilder";

const CATEGORY_ICONS: Record<string, string> = {
  burger:"🍔",burgers:"🍔",chicken:"🍗",sandwich:"🥪",sandwiches:"🥪",subs:"🥪",
  salad:"🥗",salads:"🥗",side:"🍟",sides:"🍟",fries:"🍟",drink:"🥤",drinks:"🥤",
  beverages:"🥤",breakfast:"🍳",dessert:"🍨",desserts:"🍨",pizza:"🍕",taco:"🌮",
  tacos:"🌮",burrito:"🌯",burritos:"🌯",bowl:"🥣",bowls:"🥣",wrap:"🫔",wraps:"🫔",
  ingredient:"🥘",ingredients:"🥘",protein:"🥩",proteins:"🥩",rice:"🍚",bean:"🫘",
  beans:"🫘",salsa:"🌶️",topping:"🧂",toppings:"🧂",soup:"🍲",soups:"🍲",fish:"🐟",
  seafood:"🦞",pasta:"🍝",coffee:"☕",bakery:"🥐",snack:"🍿",appetizer:"🫙",
  steak:"🥩",steaks:"🥩",wing:"🍗",wings:"🍗",nugget:"🍗",nuggets:"🍗",shake:"🥛",
  shakes:"🥛",pancake:"🥞",pancakes:"🥞",omelette:"🍳",omelettes:"🍳",slam:"🍳",
  slams:"🍳",tender:"🍗",tenders:"🍗",blizzard:"🍦",blizzards:"🍦",gyro:"🥙",
  gyros:"🥙",quesadilla:"🧀",quesadillas:"🧀",flatbread:"🫓",flatbreads:"🫓",
  "market fresh":"🥗",combo:"📦",combos:"📦",strips:"🍗",footlongs:"🥖",
};

function getCategoryIcon(name: string): string {
  const lower = name.toLowerCase();
  for (const [key, icon] of Object.entries(CATEGORY_ICONS)) {
    if (lower.includes(key)) return icon;
  }
  return "🍽️";
}

function PresetSection({ title, subtitle, presets, accentClass = "", onAdd }: {
  title: string; subtitle?: string; presets: PresetMeal[];
  accentClass?: string; onAdd: (e: { item: MenuItem; quantity: number }[]) => void;
}) {
  return (
    <div className={`mb-8 rounded-2xl p-5 border ${accentClass || "border-gray-100 bg-gray-50"}`}>
      <div className="mb-4">
        <h2 className="font-semibold text-lg text-gray-900">{title}</h2>
        {subtitle && <p className="text-xs text-gray-500 mt-0.5">{subtitle}</p>}
      </div>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        {presets.map((p) => (
          <PresetMealCard key={p.id} preset={p} onAddToMeal={onAdd} />
        ))}
      </div>
    </div>
  );
}

const SORT_OPTIONS: { value: SortOption; label: string }[] = [
  { value: "healthiest",    label: "Healthiest first" },
  { value: "unhealthiest",  label: "Most indulgent"   },
  { value: "calories_asc",  label: "Lowest calories"  },
  { value: "calories_desc", label: "Highest calories" },
  { value: "protein_desc",  label: "Highest protein"  },
  { value: "carbs_asc",     label: "Lowest carbs"     },
  { value: "sodium_asc",    label: "Lowest sodium"    },
  { value: "fat_asc",       label: "Lowest fat"       },
];

const BUILDER_TRIGGERS = ["burrito","bowl","taco","salad","quesadilla","wrap","sub","slider"];

export default function RestaurantPage() {
  const { id } = useParams<{ id: string }>();
  const chainId = Number(id);
  const router  = useRouter();

  const [selectedCategory, setSelectedCategory] = useState<number | null>(null);
  const [sort,    setSort]    = useState<SortOption>("healthiest");
  const [maxCal,  setMaxCal]  = useState<number | undefined>();
  const [searchQ, setSearchQ] = useState("");
  const [mealItems, setMealItems] = useState<MenuItem[]>([]);

  const { data: chain, isLoading: chainLoading } = useQuery({
    queryKey: ["chain", chainId],
    queryFn:  () => api.chains.get(chainId),
  });

  const { data: categories = [] } = useQuery({
    queryKey: ["categories", chainId],
    queryFn:  () => api.menu.categories(chainId),
  });

  const { data: builderConfig } = useQuery({
    queryKey: ["builder", chainId],
    queryFn:  () => api.builder.config(chainId),
    staleTime: 300_000,
  });

  const { data: popularPresets = [] } = useQuery({
    queryKey: ["presets-popular", chainId],
    queryFn:  () => api.presets.list(chainId, "popular"),
    staleTime: 300_000,
  });

  const { data: healthyPresets = [] } = useQuery({
    queryKey: ["presets-healthy", chainId],
    queryFn:  () => api.presets.list(chainId, "healthy"),
    staleTime: 300_000,
  });

  const { data: items = [], isLoading: itemsLoading } = useQuery({
    queryKey: ["menu-items", chainId, sort, selectedCategory, maxCal, searchQ],
    queryFn:  () => api.menu.list({
      chain_id:     chainId,
      sort,
      category_id:  selectedCategory ?? undefined,
      max_calories: maxCal,
      q:            searchQ || undefined,
      limit:        150,
    }),
    staleTime: 30_000,
  });

  const isBuilderChain = builderConfig?.has_builder === true;
  const selectedCat    = categories.find((c) => c.id === selectedCategory);
  const showBuilder    = isBuilderChain && selectedCat &&
    BUILDER_TRIGGERS.some((k) => selectedCat.name.toLowerCase().includes(k));

  const addToMeal = (item: MenuItem) => setMealItems((p) => [...p, item]);
  const addPreset = (entries: { item: MenuItem; quantity: number }[]) =>
    entries.forEach(({ item, quantity }) => {
      for (let i = 0; i < quantity; i++) setMealItems((p) => [...p, item]);
    });

  if (chainLoading) {
    return <div className="flex justify-center py-20"><Loader2 className="w-8 h-8 animate-spin text-brand-600" /></div>;
  }

  return (
    <div className="max-w-5xl mx-auto px-4 py-8">

      {/* Header */}
      <div className="flex items-start justify-between mb-6 gap-4">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">{chain?.name}</h1>
          <p className="text-gray-500 mt-1 text-sm">
            {chain?.cuisine_type} · {chain?.item_count} items · {chain?.location_count} locations
          </p>
          {chain?.website && (
            <a href={chain.website} target="_blank" rel="noopener noreferrer"
               className="text-brand-600 text-sm hover:underline">{chain.website}</a>
          )}
        </div>
        <div className="flex gap-2 flex-wrap justify-end shrink-0">
          <Link href={`/restaurants/${chainId}/locations`}
                className="flex items-center gap-1 border border-gray-300 text-sm px-3 py-2 rounded-lg hover:bg-gray-50">
            <MapPin className="w-4 h-4" /> Locations
          </Link>
          {mealItems.length > 0 && (
            <button
              onClick={() => router.push(`/meal-builder?items=${mealItems.map(i=>i.id).join(",")}`)}
              className="flex items-center gap-1 bg-brand-600 text-white text-sm px-4 py-2 rounded-lg hover:bg-brand-700"
            >
              <ShoppingCart className="w-4 h-4" /> Meal ({mealItems.length})
            </button>
          )}
        </div>
      </div>

      {/* Popular Combos */}
      {popularPresets.length > 0 && (
        <PresetSection title="⚡ Popular Combos" presets={popularPresets} onAdd={addPreset} />
      )}

      {/* Healthiest Options */}
      {healthyPresets.length > 0 && (
        <PresetSection
          title="🥗 Healthiest Options"
          subtitle="Lowest health score · Fewest calories · Highest protein"
          accentClass="border-green-200 bg-green-50"
          presets={healthyPresets}
          onAdd={addPreset}
        />
      )}

      {/* ── Category grid — ALL chains ──────────────────────────────────── */}
      {categories.length > 0 && (
        <div className="mb-6">
          <p className="text-xs font-semibold text-gray-500 uppercase tracking-wide mb-3">Browse Menu</p>
          <div className="grid grid-cols-3 sm:grid-cols-4 md:grid-cols-5 lg:grid-cols-6 gap-2">
            <button
              onClick={() => setSelectedCategory(null)}
              className={`flex flex-col items-center gap-1 rounded-xl border-2 p-3 text-center transition-all
                ${selectedCategory === null ? "border-brand-500 bg-brand-50" : "border-gray-200 bg-white hover:border-brand-300"}`}
            >
              <span className="text-2xl">🍽️</span>
              <span className="text-xs font-medium text-gray-700">All</span>
            </button>
            {categories.map((cat) => (
              <button
                key={cat.id}
                onClick={() => setSelectedCategory(cat.id === selectedCategory ? null : cat.id)}
                className={`flex flex-col items-center gap-1 rounded-xl border-2 p-3 text-center transition-all
                  ${selectedCategory === cat.id ? "border-brand-500 bg-brand-50" : "border-gray-200 bg-white hover:border-brand-300"}`}
              >
                <span className="text-2xl">{getCategoryIcon(cat.name)}</span>
                <span className="text-xs font-medium text-gray-700 leading-tight">{cat.name}</span>
              </button>
            ))}
          </div>
        </div>
      )}

      {/* ── Ingredient Builder ──────────────────────────────────────────── */}
      {showBuilder && builderConfig && (
        <div className="bg-white border border-gray-200 rounded-2xl p-6 mb-6">
          <h2 className="font-bold text-xl mb-1">
            Build Your {selectedCat!.name.replace(/s$/i, "")}
          </h2>
          <p className="text-gray-500 text-sm mb-6">
            Pick your ingredients — nutrition updates live as you choose
          </p>
          <IngredientBuilder
            config={builderConfig}
            chainName={chain?.name ?? ""}
            onAddToMeal={(group: BuiltMealGroup) => {
              const existing: BuiltMealGroup[] = JSON.parse(
                sessionStorage.getItem("mealGroups") || "[]"
              );
              sessionStorage.setItem("mealGroups", JSON.stringify([...existing, group]));
              router.push("/meal-builder");
            }}
          />
        </div>
      )}

      {/* ── Item list ───────────────────────────────────────────────────── */}
      {!showBuilder && (
        <>
          <div className="bg-white border border-gray-200 rounded-xl p-4 mb-4 flex flex-wrap gap-3 items-end">
            <div>
              <label className="text-xs text-gray-500 block mb-1">Sort by</label>
              <select
                value={sort}
                onChange={(e) => setSort(e.target.value as SortOption)}
                className="border rounded-lg px-3 py-1.5 text-sm focus:outline-none focus:ring-2 focus:ring-brand-500"
              >
                {SORT_OPTIONS.map((o) => (
                  <option key={o.value} value={o.value}>{o.label}</option>
                ))}
              </select>
            </div>
            <div>
              <label className="text-xs text-gray-500 block mb-1">Max calories</label>
              <input
                type="number" placeholder="e.g. 500" value={maxCal ?? ""}
                onChange={(e) => setMaxCal(e.target.value ? Number(e.target.value) : undefined)}
                className="border rounded-lg px-3 py-1.5 text-sm w-28 focus:outline-none focus:ring-2 focus:ring-brand-500"
              />
            </div>
            <div className="flex-1 min-w-[160px]">
              <label className="text-xs text-gray-500 block mb-1">Search items</label>
              <input
                type="text" placeholder="e.g. grilled, salad…" value={searchQ}
                onChange={(e) => setSearchQ(e.target.value)}
                className="w-full border rounded-lg px-3 py-1.5 text-sm focus:outline-none focus:ring-2 focus:ring-brand-500"
              />
            </div>
          </div>

          {selectedCat && (
            <div className="flex items-center gap-2 mb-4">
              <span className="text-2xl">{getCategoryIcon(selectedCat.name)}</span>
              <h2 className="font-semibold text-lg text-gray-900">{selectedCat.name}</h2>
              <span className="text-sm text-gray-400">({items.length} items)</span>
              <button onClick={() => setSelectedCategory(null)} className="ml-auto text-xs text-gray-400 hover:text-brand-600 underline">
                Show all
              </button>
            </div>
          )}

          {itemsLoading ? (
            <div className="flex justify-center py-12"><Loader2 className="w-8 h-8 animate-spin text-brand-600" /></div>
          ) : items.length === 0 ? (
            <p className="text-center text-gray-400 py-12">No menu items found.</p>
          ) : (
            <div className="grid gap-3">
              {items.map((item) => (
                <MenuItemCard key={item.id} item={item} onAddToMeal={addToMeal} />
              ))}
            </div>
          )}
        </>
      )}
    </div>
  );
}
