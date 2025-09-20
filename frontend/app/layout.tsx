import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: {
    default: "Sentinel AI — AI-Driven Cyber Defense",
    template: "%s — Sentinel AI",
  },
  description:
    "Real-time threat detection, automated incident response, and decision support for modern cloud and enterprise environments.",
  openGraph: {
    title: "Sentinel AI",
    description:
      "Real-time threat detection, automated incident response, and decision support for modern cloud and enterprise environments.",
    url: "https://localhost:3000",
    siteName: "Sentinel AI",
    images: [],
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "Sentinel AI",
    description:
      "Real-time threat detection, automated incident response, and decision support for modern cloud and enterprise environments.",
  },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="min-h-screen antialiased bg-white text-slate-800">
        {children}
      </body>
    </html>
  );
}
