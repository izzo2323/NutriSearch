"use client";
import { useState, useCallback } from "react";
import { useQuery } from "@tanstack/react-query";
import { Search, MapPin, Loader2 } from "lucide-react";
import Link from "next/link";
import { api } from "@/lib/api";
import type { Location } from "@/lib/types";
import dynamic from "next/dynamic";

const LocationMap = dynamic(() => import("@/components/LocationMap"), { ssr: false });

const CUISINE_FILTERS = [
  "All", "Fast Food", "Mexican", "Pizza", "Coffee / Café",
  "Casual Dining", "Breakfast", "Sandwiches", "Wings", "Asian", "Seafood", "Italian",
];

export default function HomePage() {
  const [searchQ, setSearchQ]         = useState("");
  const [cuisine, setCuisine]         = useState("All");
  const [locationQuery, setLocationQ] = useState("");
  const [nearbyCenter, setNearbyCenter] = useState<[number, number] | null>(null);
  const [nearbyLocations, setNearbyLocations] = useState<Location[]>([]);
  const [geoLoading, setGeoLoading]   = useState(false);
  const [geoError, setGeoError]       = useState("");

  const { data: chains = [], isLoading } = useQuery({
    queryKey: ["chains", searchQ, cuisine],
    queryFn: () => api.chains.list(searchQ || undefined, cuisine === "All" ? undefined : cuisine),
    staleTime: 60_000,
  });

  const handleGPS = useCallback(() => {
    if (!navigator.geolocation) return;
    setGeoLoading(true);
    setGeoError("");
    navigator.geolocation.getCurrentPosition(
      async (pos) => {
        const { latitude: lat, longitude: lon } = pos.coords;
        const locs = await api.chains.near(lat, lon, 25);
        setNearbyCenter([lat, lon]);
        setNearbyLocations(locs);
        setGeoLoading(false);
      },
      () => {
        setGeoError("Location access denied.");
        setGeoLoading(false);
      },
    );
  }, []);

  const handleCitySearch = useCallback(async () => {
    if (!locationQuery.trim()) return;
    setGeoLoading(true);
    setGeoError("");
    const result = await api.locations.geocode(locationQuery);
    if ("error" in result) {
      setGeoError(result.error);
      setGeoLoading(false);
      return;
    }
    const { lat, lon } = result;
    const locs = await api.chains.near(lat, lon, 25);
    setNearbyCenter([lat, lon]);
    setNearbyLocations(locs);
    setGeoLoading(false);
  }, [locationQuery]);

  return (
    <div className="max-w-7xl mx-auto px-4 py-8">
      {/* Hero */}
      <div className="text-center mb-10">
        <h1 className="text-4xl font-bold text-gray-900 mb-2">Restaurant Nutrition Database</h1>
        <p className="text-gray-500 text-lg">Search 50+ chains. Sort by healthiest. Build your meal.</p>
      </div>

      {/* Restaurant search */}
      <div className="flex gap-2 mb-4">
        <div className="relative flex-1">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" />
          <input
            type="text"
            placeholder="Search restaurant name…"
            className="w-full border rounded-lg pl-9 pr-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-brand-500"
            value={searchQ}
            onChange={(e) => setSearchQ(e.target.value)}
          />
        </div>
      </div>

      {/* Cuisine filter chips */}
      <div className="flex flex-wrap gap-2 mb-8">
        {CUISINE_FILTERS.map((c) => (
          <button
            key={c}
            onClick={() => setCuisine(c)}
            className={`text-xs px-3 py-1 rounded-full border transition-colors ${
              cuisine === c
                ? "bg-brand-600 text-white border-brand-600"
                : "bg-white text-gray-600 border-gray-300 hover:border-brand-500"
            }`}
          >
            {c}
          </button>
        ))}
      </div>

      {/* Restaurant grid */}
      {isLoading ? (
        <div className="flex justify-center py-12">
          <Loader2 className="w-8 h-8 animate-spin text-brand-600" />
        </div>
      ) : (
        <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4 mb-12">
          {chains.map((chain) => (
            <Link
              key={chain.id}
              href={`/restaurants/${chain.id}`}
              className="bg-white border border-gray-200 rounded-xl p-4 hover:shadow-md hover:border-brand-400 transition-all flex flex-col items-center text-center gap-2"
            >
              <div className="w-12 h-12 bg-brand-100 rounded-full flex items-center justify-center text-brand-700 font-bold text-lg">
                {chain.name.charAt(0)}
              </div>
              <span className="font-medium text-sm text-gray-800 leading-tight">{chain.name}</span>
              <span className="text-xs text-gray-400">{chain.cuisine_type}</span>
              <span className="text-xs text-gray-500">{chain.item_count} items</span>
            </Link>
          ))}
          {chains.length === 0 && (
            <p className="col-span-full text-center text-gray-400 py-8">
              No restaurants found. Run the scraper first to populate the database.
            </p>
          )}
        </div>
      )}

      {/* Location search */}
      <div className="bg-white border border-gray-200 rounded-xl p-6">
        <h2 className="font-semibold text-lg mb-4 flex items-center gap-2">
          <MapPin className="w-5 h-5 text-brand-600" />
          Find Restaurants Near You
        </h2>
        <div className="flex gap-2 mb-3">
          <input
            type="text"
            placeholder="City, zip code, or address…"
            className="flex-1 border rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-brand-500"
            value={locationQuery}
            onChange={(e) => setLocationQ(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleCitySearch()}
          />
          <button
            onClick={handleCitySearch}
            className="bg-brand-600 text-white px-4 py-2 rounded-lg text-sm hover:bg-brand-700"
          >
            Search
          </button>
          <button
            onClick={handleGPS}
            disabled={geoLoading}
            className="flex items-center gap-1 border border-brand-600 text-brand-600 px-3 py-2 rounded-lg text-sm hover:bg-brand-50 disabled:opacity-50"
          >
            {geoLoading ? <Loader2 className="w-4 h-4 animate-spin" /> : <MapPin className="w-4 h-4" />}
            Use GPS
          </button>
        </div>
        {geoError && <p className="text-red-500 text-sm mb-2">{geoError}</p>}

        {nearbyCenter && (
          <>
            <LocationMap center={nearbyCenter} locations={nearbyLocations} />
            <div className="mt-4 grid grid-cols-1 sm:grid-cols-2 gap-2">
              {nearbyLocations.slice(0, 20).map((loc) => (
                <Link
                  key={loc.id}
                  href={`/restaurants/${loc.chain_id}`}
                  className="flex justify-between items-center border rounded-lg px-3 py-2 hover:bg-brand-50 text-sm"
                >
                  <div>
                    <span className="font-medium">{loc.chain?.name}</span>
                    <p className="text-xs text-gray-500">{loc.address}, {loc.city}</p>
                  </div>
                  <span className="text-xs text-gray-400">{loc.distance_km} km</span>
                </Link>
              ))}
            </div>
          </>
        )}
      </div>
    </div>
  );
}
