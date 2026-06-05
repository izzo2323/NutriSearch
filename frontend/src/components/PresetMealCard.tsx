"use client";
import { useRouter } from "next/navigation";
import { Zap } from "lucide-react";
import type { PresetMeal, MenuItem } from "@/lib/types";

interface Props {
  preset: PresetMeal;
  onAddToMeal?: (items: { item: MenuItem; quantity: number }[]) => void;
}

function calColor(cal: number) {
  if (cal < 600)  return "text-green-700 bg-green-50";
  if (cal < 1000) return "text-yellow-700 bg-yellow-50";
  return "text-red-700 bg-red-50";
}

export default function PresetMealCard({ preset, onAddToMeal }: Props) {
  const router  = useRouter();
  const totals  = preset.totals;
  const cal     = totals?.calories ?? 0;

  const handleAdd = () => {
    if (onAddToMeal) {
      onAddToMeal(
        preset.items.map((pi) => ({ item: pi.menu_item, quantity: pi.quantity }))
      );
    } else {
      // Navigate to meal builder with all item IDs pre-filled
      const ids = preset.items
        .flatMap((pi) => Array(pi.quantity).fill(pi.menu_item.id))
        .join(",");
      router.push(`/meal-builder?items=${ids}`);
    }
  };

  return (
    <div className="bg-white border border-gray-200 rounded-xl p-4 flex flex-col gap-3 hover:shadow-md hover:border-brand-300 transition-all">
      <div className="flex items-start justify-between gap-2">
        <div>
          <h3 className="font-semibold text-gray-900 text-sm">{preset.name}</h3>
          {preset.description && (
            <p className="text-xs text-gray-500 mt-0.5 leading-snug">{preset.description}</p>
          )}
        </div>
        <span className={`text-xs font-bold px-2 py-1 rounded-full whitespace-nowrap ${calColor(cal)}`}>
          {cal} cal
        </span>
      </div>

      {/* Item list */}
      <ul className="text-xs text-gray-600 space-y-0.5">
        {preset.items.map((pi, i) => (
          <li key={i} className="flex gap-1">
            {pi.quantity > 1 && <span className="font-semibold">×{pi.quantity}</span>}
            <span>{pi.menu_item.name}</span>
          </li>
        ))}
      </ul>

      {/* Quick macro row */}
      {totals && (
        <div className="flex gap-3 text-xs text-gray-500 border-t border-gray-100 pt-2">
          <span><b className="text-gray-700">{totals.protein_g.toFixed(0)}g</b> protein</span>
          <span><b className="text-gray-700">{totals.total_carbs_g.toFixed(0)}g</b> carbs</span>
          <span><b className="text-gray-700">{totals.total_fat_g.toFixed(0)}g</b> fat</span>
          <span><b className="text-gray-700">{totals.total_sugars_g.toFixed(0)}g</b> sugar</span>
        </div>
      )}

      <button
        onClick={handleAdd}
        className="flex items-center justify-center gap-1.5 w-full bg-brand-600 text-white text-xs font-medium py-1.5 rounded-lg hover:bg-brand-700 transition-colors"
      >
        <Zap className="w-3.5 h-3.5" />
        Add to Meal Builder
      </button>
    </div>
  );
}
