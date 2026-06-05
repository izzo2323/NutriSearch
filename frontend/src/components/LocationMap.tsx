"use client";
import { useEffect, useRef } from "react";
import type { Location } from "@/lib/types";

interface Props {
  center: [number, number];
  locations: Location[];
}

export default function LocationMap({ center, locations }: Props) {
  const mapRef = useRef<HTMLDivElement>(null);
  const mapInstanceRef = useRef<unknown>(null);

  useEffect(() => {
    if (!mapRef.current || mapInstanceRef.current) return;

    // Dynamic import to avoid SSR issues
    import("leaflet").then((L) => {
      // Fix marker icon paths broken by webpack
      delete (L.Icon.Default.prototype as any)._getIconUrl;
      L.Icon.Default.mergeOptions({
        iconRetinaUrl: "https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon-2x.png",
        iconUrl:       "https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png",
        shadowUrl:     "https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png",
      });

      const map = L.map(mapRef.current!).setView(center, 12);
      mapInstanceRef.current = map;

      L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution: "© OpenStreetMap contributors",
        maxZoom: 19,
      }).addTo(map);

      locations.forEach((loc) => {
        if (!loc.lat || !loc.lon) return;
        const popup = [
          `<b>${loc.chain?.name ?? "Restaurant"}</b>`,
          loc.address,
          `${loc.city ?? ""}, ${loc.state ?? ""}`,
          loc.distance_km !== null ? `${loc.distance_km} km away` : "",
        ].filter(Boolean).join("<br>");

        L.marker([Number(loc.lat), Number(loc.lon)])
          .addTo(map)
          .bindPopup(popup);
      });
    });

    return () => {
      if (mapInstanceRef.current) {
        (mapInstanceRef.current as any).remove();
        mapInstanceRef.current = null;
      }
    };
  }, [center, locations]);

  return <div ref={mapRef} className="h-80 w-full rounded-lg z-0" />;
}
