import Link from "next/link";
import { Salad } from "lucide-react";

export default function Navbar() {
  return (
    <nav className="bg-brand-700 text-white shadow-md">
      <div className="max-w-7xl mx-auto px-4 py-3 flex items-center gap-6">
        <Link href="/" className="flex items-center gap-2 font-bold text-xl">
          <Salad className="w-6 h-6" />
          NutriSearch
        </Link>
        <Link href="/" className="text-sm hover:text-brand-100">Restaurants</Link>
        <Link href="/meal-builder" className="text-sm hover:text-brand-100">Meal Builder</Link>
      </div>
    </nav>
  );
}
