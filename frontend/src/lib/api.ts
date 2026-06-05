import type {
  ChainDetail, MenuItem, Location, MealAnalysis, SortOption
} from "./types";

const BASE = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

async function get<T>(path: string, params?: Record<string, string | number | undefined>): Promise<T> {
  const url = new URL(`${BASE}/api${path}`);
  if (params) {
    Object.entries(params).forEach(([k, v]) => {
      if (v !== undefined) url.searchParams.set(k, String(v));
    });
  }
  const res = await fetch(url.toString(), { next: { revalidate: 300 } });
  if (!res.ok) throw new Error(`API error ${res.status}: ${path}`);
  return res.json();
}

async function post<T>(path: string, body: unknown): Promise<T> {
  const res = await fetch(`${BASE}/api${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  if (!res.ok) throw new Error(`API error ${res.status}: ${path}`);
  return res.json();
}

export const api = {
  chains: {
    list: (q?: string, cuisine?: string) =>
      get<ChainDetail[]>("/restaurants", { q, cuisine }),
    get: (id: number) =>
      get<ChainDetail>(`/restaurants/${id}`),
    near: (lat: number, lon: number, radius_km = 25) =>
      get<Location[]>("/restaurants/near", { lat, lon, radius_km }),
  },

  menu: {
    list: (params: {
      q?: string;
      chain_id?: number;
      category_id?: number;
      sort?: SortOption;
      max_calories?: number;
      limit?: number;
      offset?: number;
    }) => get<MenuItem[]>("/menu-items", params),
    get: (id: number) => get<MenuItem>(`/menu-items/${id}`),
    categories: (chainId: number) =>
      get<{ id: number; name: string }[]>(`/menu-items/chain/${chainId}/categories`),
  },

  locations: {
    geocode: (q: string) =>
      get<{ lat: number; lon: number; display_name: string } | { error: string }>("/locations/geocode", { q }),
    forChain: (chainId: number) =>
      get<Location[]>(`/locations/chain/${chainId}`),
  },

  meal: {
    analyze: (items: { menu_item_id: number; quantity: number }[]) =>
      post<MealAnalysis>("/meal/analyze", { items }),
  },

  presets: {
    list: (chainId?: number, category?: string) =>
      get<import("./types").PresetMeal[]>("/preset-meals", { chain_id: chainId, category }),
  },

  builder: {
    config: (chainId: number) =>
      get<import("./types").BuilderConfig>(`/builder/${chainId}`),
  },
};
