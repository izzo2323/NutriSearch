"use client";
import Link from "next/link";
import { Plus } from "lucide-react";
import type { MenuItem } from "@/lib/types";
import CalorieBadge from "./CalorieBadge";

interface Props {
  item: MenuItem;
  onAddToMeal?: (item: MenuItem) => void;
}

export default function MenuItemCard({ item, onAddToMeal }: Props) {
  const n = item.nutrition;

  return (
    <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-4 hover:border-brand-300 transition-colors">
      <div className="flex justify-between items-start gap-2">
        <div className="flex-1">
          <Link
            href={`/menu-items/${item.id}`}
            className="font-semibold text-gray-900 hover:text-brand-700 hover:underline"
          >
            {item.name}
          </Link>
          {item.description && (
            <p className="text-xs text-gray-500 mt-0.5 line-clamp-2">{item.description}</p>
          )}
          <div className="flex gap-3 mt-2 text-xs text-gray-600">
            {n?.protein_g      != null && <span><b>{n.protein_g}g</b> protein</span>}
            {n?.total_carbs_g  != null && <span><b>{n.total_carbs_g}g</b> carbs</span>}
            {n?.total_fat_g    != null && <span><b>{n.total_fat_g}g</b> fat</span>}
            {n?.total_sugars_g != null && <span><b>{n.total_sugars_g}g</b> sugar</span>}
          </div>
        </div>
        <div className="flex flex-col items-end gap-2">
          <CalorieBadge calories={n?.calories ?? null} />
          {onAddToMeal && (
            <button
              onClick={() => onAddToMeal(item)}
              className="flex items-center gap-1 text-xs bg-brand-600 text-white px-2 py-1 rounded hover:bg-brand-700"
            >
              <Plus className="w-3 h-3" /> Add
            </button>
          )}
        </div>
      </div>
    </div>
  );
}
