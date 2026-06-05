export default function CalorieBadge({ calories }: { calories: number | null }) {
  if (calories === null) return <span className="text-gray-400 text-xs">—</span>;
  const cls =
    calories < 300 ? "calorie-low" :
    calories < 600 ? "calorie-medium" :
    "calorie-high";
  return (
    <span className={`${cls} text-xs font-semibold px-2 py-0.5 rounded-full`}>
      {calories} cal
    </span>
  );
}
