import type { Metadata } from "next";
import "./globals.css";
import QueryProvider from "@/components/QueryProvider";
import Navbar from "@/components/Navbar";

export const metadata: Metadata = {
  title: "NutriSearch — Restaurant Nutrition Database",
  description: "Search, compare, and plan meals with full nutrition data for 50+ restaurant chains.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <QueryProvider>
          <Navbar />
          <main className="min-h-screen">{children}</main>
        </QueryProvider>
      </body>
    </html>
  );
}
