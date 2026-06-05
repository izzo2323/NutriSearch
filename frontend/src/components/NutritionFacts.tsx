import type { Nutrition } from "@/lib/types";

function Row({ label, value, unit, indent = false }: {
  label: string; value: number | null; unit: string; indent?: boolean;
}) {
  return (
    <div className={`flex justify-between py-0.5 ${indent ? "pl-4 text-sm" : "font-semibold"}`}>
      <span>{label}</span>
      <span>{value ?? "—"}{value !== null ? unit : ""}</span>
    </div>
  );
}

export default function NutritionFacts({ n, servingSize }: { n: Nutrition; servingSize?: string | null }) {
  return (
    <div className="border-2 border-black p-3 font-mono text-sm max-w-sm">
      <h2 className="text-3xl font-black border-b-8 border-black pb-1">Nutrition Facts</h2>
      {servingSize && <p className="text-xs mt-1">Serving size: {servingSize}</p>}

      <div className="border-b-4 border-black mt-2 pb-2">
        <p className="text-xs">Amount per serving</p>
        <div className="flex justify-between items-baseline">
          <span className="font-black text-lg">Calories</span>
          <span className="font-black text-4xl">{n.calories ?? "—"}</span>
        </div>
      </div>

      <div className="border-b border-black py-1 text-right text-xs">% Daily Value*</div>

      <Row label="Total Fat"       value={n.total_fat_g}       unit="g" />
      <Row label="Saturated Fat"   value={n.saturated_fat_g}   unit="g" indent />
      <Row label="Trans Fat"       value={n.trans_fat_g}       unit="g" indent />
      <Row label="Cholesterol"     value={n.cholesterol_mg}    unit="mg" />
      <Row label="Sodium"          value={n.sodium_mg}         unit="mg" />
      <Row label="Total Carbohydrate" value={n.total_carbs_g}  unit="g" />
      <Row label="Dietary Fiber"   value={n.dietary_fiber_g}   unit="g" indent />
      <Row label="Total Sugars"    value={n.total_sugars_g}    unit="g" indent />
      {n.added_sugars_g !== null && (
        <Row label="  Added Sugars" value={n.added_sugars_g}   unit="g" indent />
      )}
      <Row label="Protein"         value={n.protein_g}         unit="g" />

      <div className="border-t-4 border-black mt-2 pt-1 text-xs space-y-0.5">
        {n.vitamin_d_mcg  !== null && <div>Vitamin D {n.vitamin_d_mcg}mcg</div>}
        {n.calcium_mg     !== null && <div>Calcium {n.calcium_mg}mg</div>}
        {n.iron_mg        !== null && <div>Iron {n.iron_mg}mg</div>}
        {n.potassium_mg   !== null && <div>Potassium {n.potassium_mg}mg</div>}
      </div>

      <p className="text-xs mt-2 border-t border-black pt-1">
        *Percent Daily Values are based on a 2,000 calorie diet.
      </p>
    </div>
  );
}
