"use client";
import { useState, useMemo } from "react";
import { useRouter } from "next/navigation";
import { ShoppingCart, Check } from "lucide-react";
import type { BuilderMealType, BuilderIngredientGroup, BuilderConfig, MenuItem } from "@/lib/types";
import CalorieBadge from "./CalorieBadge";

function n(val: number | string | null | undefined) {
  return val == null ? 0 : Number(val);
}

export interface BuiltMealGroup {
  label:    string;
  icon:     string;
  itemIds:  number[];
}

interface Props {
  config:       BuilderConfig;
  chainName:    string;
  onAddToMeal?: (group: BuiltMealGroup) => void;
}

export default function IngredientBuilder({ config, chainName, onAddToMeal }: Props) {
  const router = useRouter();
  const [selectedType, setSelectedType]       = useState<BuilderMealType | null>(null);
  const [selections, setSelections]            = useState<Record<string, string[]>>({});

  const meal_types        = config.meal_types        ?? [];
  const ingredient_groups = config.ingredient_groups ?? [];

  // ── toggle a selection ──────────────────────────────────────────────────
  const toggle = (groupId: string, itemName: string, max: number) => {
    setSelections((prev) => {
      const current = prev[groupId] ?? [];
      if (current.includes(itemName)) {
        return { ...prev, [groupId]: current.filter((n) => n !== itemName) };
      }
      if (max === 1) {
        return { ...prev, [groupId]: [itemName] };
      }
      if (current.length >= max) return prev;
      return { ...prev, [groupId]: [...current, itemName] };
    });
  };

  const selectNone = (groupId: string) =>
    setSelections((prev) => ({ ...prev, [groupId]: [] }));

  // ── collect all selected MenuItem objects ───────────────────────────────
  const selectedItems = useMemo((): MenuItem[] => {
    if (!selectedType) return [];
    const result: MenuItem[] = [];

    // base items (tortilla, shells, etc.)
    for (const slot of selectedType.base_items) {
      if (slot.item) result.push(slot.item);
    }

    // ingredient selections
    for (const grp of ingredient_groups) {
      const chosen = selections[grp.id] ?? [];
      for (const name of chosen) {
        const slot = grp.items.find((s) => s.name === name);
        if (slot?.item) result.push(slot.item);
      }
    }
    return result;
  }, [selectedType, selections, ingredient_groups]);

  // ── running nutrition total ──────────────────────────────────────────────
  const totals = useMemo(() => {
    return selectedItems.reduce(
      (acc, item) => {
        const nu = item.nutrition;
        if (!nu) return acc;
        return {
          calories: acc.calories + n(nu.calories),
          protein:  acc.protein  + n(nu.protein_g),
          carbs:    acc.carbs    + n(nu.total_carbs_g),
          fat:      acc.fat      + n(nu.total_fat_g),
          sugar:    acc.sugar    + n(nu.total_sugars_g),
          sodium:   acc.sodium   + n(nu.sodium_mg),
        };
      },
      { calories: 0, protein: 0, carbs: 0, fat: 0, sugar: 0, sodium: 0 }
    );
  }, [selectedItems]);

  const isValid = selectedType !== null &&
    ingredient_groups
      .filter((g) => g.required)
      .every((g) => (selections[g.id]?.length ?? 0) > 0);

  const handleAdd = () => {
    if (!isValid || !selectedType) return;
    const group: BuiltMealGroup = {
      label:   `${chainName} ${selectedType.name}`,
      icon:    selectedType.icon,
      itemIds: selectedItems.map((i) => i.id),
    };
    if (onAddToMeal) {
      onAddToMeal(group);
    } else {
      // Direct navigation — store group and go to meal builder
      const existing: BuiltMealGroup[] = JSON.parse(sessionStorage.getItem("mealGroups") || "[]");
      sessionStorage.setItem("mealGroups", JSON.stringify([...existing, group]));
      router.push("/meal-builder");
    }
  };

  // ── reset when meal type changes ──────────────────────────────────────────
  const pickMealType = (mt: BuilderMealType) => {
    setSelectedType(mt);
    setSelections({});
  };

  return (
    <div className="space-y-6">
      {/* Step 1 — Meal type */}
      <div>
        <h3 className="text-sm font-semibold text-gray-500 uppercase tracking-wide mb-3">
          Choose Your Meal
        </h3>
        <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
          {meal_types.map((mt) => {
            const active = selectedType?.id === mt.id;
            return (
              <button
                key={mt.id}
                onClick={() => pickMealType(mt)}
                className={`flex flex-col items-center gap-1.5 rounded-xl border-2 p-4 transition-all text-center
                  ${active
                    ? "border-brand-500 bg-brand-50 shadow-sm"
                    : "border-gray-200 bg-white hover:border-brand-300"
                  }`}
              >
                <span className="text-3xl">{mt.icon}</span>
                <span className="font-semibold text-sm text-gray-900">{mt.name}</span>
                <span className="text-xs text-gray-500 leading-tight">{mt.description}</span>
                {mt.base_items.length > 0 && (
                  <span className="text-xs text-gray-400">
                    +{mt.base_items.reduce((s, b) => s + n(b.item?.nutrition?.calories), 0)} cal base
                  </span>
                )}
              </button>
            );
          })}
        </div>
      </div>

      {/* Steps 2+ — Ingredient groups (only shown after meal type is chosen) */}
      {selectedType && ingredient_groups.map((grp, idx) => {
        const chosen  = selections[grp.id] ?? [];
        const isRadio = grp.max_selections === 1;

        return (
          <div key={grp.id} className="border border-gray-100 rounded-xl overflow-hidden">
            {/* Group header */}
            <div className="bg-gray-50 px-4 py-2.5 flex items-center justify-between">
              <span className="font-semibold text-sm text-gray-800">
                Step {idx + 2}: {grp.name}
                {grp.required && <span className="text-red-400 ml-1">*</span>}
              </span>
              <span className="text-xs text-gray-400">
                {isRadio ? "Pick one" : `Pick up to ${grp.max_selections}`}
              </span>
            </div>

            <div className="p-3 flex flex-wrap gap-2">
              {/* None option */}
              {grp.none_label && (
                <button
                  onClick={() => selectNone(grp.id)}
                  className={`flex items-center gap-1.5 px-3 py-2 rounded-lg border text-sm transition-all
                    ${chosen.length === 0
                      ? "border-brand-500 bg-brand-50 text-brand-700 font-medium"
                      : "border-gray-200 bg-white text-gray-600 hover:border-gray-300"
                    }`}
                >
                  {chosen.length === 0 && <Check className="w-3.5 h-3.5" />}
                  {grp.none_label}
                </button>
              )}

              {grp.items.map((slot) => {
                const active   = chosen.includes(slot.name);
                const calories = slot.item?.nutrition?.calories ?? null;
                const disabled = !active && chosen.length >= grp.max_selections && !isRadio;

                return (
                  <button
                    key={slot.name}
                    disabled={disabled}
                    onClick={() => toggle(grp.id, slot.name, grp.max_selections)}
                    className={`flex items-center gap-1.5 px-3 py-2 rounded-lg border text-sm transition-all
                      ${active
                        ? "border-brand-500 bg-brand-50 text-brand-700 font-medium"
                        : disabled
                          ? "border-gray-100 bg-gray-50 text-gray-300 cursor-not-allowed"
                          : "border-gray-200 bg-white text-gray-700 hover:border-brand-300"
                      }`}
                  >
                    {active && <Check className="w-3.5 h-3.5" />}
                    <span>{slot.name}</span>
                    {calories !== null && (
                      <span className={`text-xs ${active ? "text-brand-500" : "text-gray-400"}`}>
                        +{calories}
                      </span>
                    )}
                    {!slot.item && (
                      <span className="text-xs text-gray-300">(no data)</span>
                    )}
                  </button>
                );
              })}
            </div>
          </div>
        );
      })}

      {/* Running total + add button */}
      {selectedType && (
        <div className={`rounded-xl p-4 transition-all ${selectedItems.length > 0 ? "bg-gray-900 text-white" : "bg-gray-50 text-gray-600"}`}>
          <div className="flex items-baseline justify-between mb-3">
            <span className={`text-sm font-medium ${selectedItems.length > 0 ? "text-gray-400" : "text-gray-400"}`}>
              {selectedType.name} Total
            </span>
            <span className="text-3xl font-black">{Math.round(totals.calories)} <span className="text-base font-normal">cal</span></span>
          </div>

          {selectedItems.length > 0 && (
            <div className="grid grid-cols-2 gap-x-4 gap-y-1 text-sm mb-4">
              {[
                ["Protein",  `${totals.protein.toFixed(1)}g`],
                ["Carbs",    `${totals.carbs.toFixed(1)}g`],
                ["Fat",      `${totals.fat.toFixed(1)}g`],
                ["Sugar",    `${totals.sugar.toFixed(1)}g`],
                ["Sodium",   `${Math.round(totals.sodium)}mg`],
              ].map(([label, val]) => (
                <div key={label} className="flex justify-between">
                  <span className="text-gray-400">{label}</span>
                  <span className="font-semibold">{val}</span>
                </div>
              ))}
            </div>
          )}

          <button
            onClick={handleAdd}
            disabled={!isValid}
            className="w-full flex items-center justify-center gap-2 bg-brand-600 text-white font-semibold py-3 rounded-xl hover:bg-brand-700 disabled:opacity-40 disabled:cursor-not-allowed transition-colors"
          >
            <ShoppingCart className="w-4 h-4" />
            {isValid ? `Add ${selectedType.name} to Meal Builder` : "Select required options above"}
          </button>

          {!isValid && selectedType && (
            <p className="text-xs text-center mt-2 text-gray-400">
              {ingredient_groups.filter((g) => g.required && !(selections[g.id]?.length)).map((g) => g.name).join(", ")} required
            </p>
          )}
        </div>
      )}
    </div>
  );
}
