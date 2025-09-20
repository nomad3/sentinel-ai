"use client";

import { useEffect, useState } from "react";

type Incident = {
  id: number;
  title: string;
  severity: string;
  status: string;
  started_at?: string | null;
};

const demo: Incident[] = [
  { id: 101, title: "Suspicious login from RU", severity: "high", status: "open", started_at: new Date().toISOString() },
  { id: 102, title: "Mass 5xx errors", severity: "medium", status: "open", started_at: new Date().toISOString() },
];

export default function LiveIncidents() {
  const [items, setItems] = useState<Incident[]>([]);

  useEffect(() => {
    const url = `${process.env.NEXT_PUBLIC_API_BASE}/api/v1/incidents/?limit=5`;
    fetch(url)
      .then((r) => r.json())
      .then((data) => setItems(Array.isArray(data) && data.length ? data : demo))
      .catch(() => setItems(demo));
  }, []);

  return (
    <section className="py-16">
      <div className="mx-auto max-w-7xl px-6">
        <h2 className="text-2xl font-semibold text-slate-900">Live Incidents</h2>
        <div className="mt-6 grid gap-4 md:grid-cols-2">
          {items.map((i) => (
            <div key={i.id} className="rounded-xl border border-slate-200 p-4 flex items-center justify-between">
              <div>
                <div className="font-semibold text-slate-900">{i.title}</div>
                <div className="text-xs text-slate-500 mt-1">#{i.id} • {i.started_at ? new Date(i.started_at).toLocaleString() : '-'}</div>
              </div>
              <span className={`inline-flex items-center rounded-full px-2 py-0.5 text-xs font-medium ${i.severity === 'critical' ? 'bg-red-100 text-red-700' : i.severity === 'high' ? 'bg-orange-100 text-orange-700' : i.severity === 'medium' ? 'bg-yellow-100 text-yellow-700' : 'bg-green-100 text-green-700'}`}>{i.severity}</span>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
