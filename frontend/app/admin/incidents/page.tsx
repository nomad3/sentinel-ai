"use client";

import { useEffect, useState } from "react";

type Incident = {
  id: number;
  title: string;
  severity: string;
  status: string;
  asset_id?: number | null;
  started_at?: string | null;
  resolved_at?: string | null;
  created_at?: string | null;
};

export default function AdminIncidents() {
  const [items, setItems] = useState<Incident[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const url = `${process.env.NEXT_PUBLIC_API_BASE}/api/v1/incidents/?limit=50`;
    fetch(url)
      .then((r) => r.json())
      .then((data) => setItems(data))
      .catch(() => setItems([]))
      .finally(() => setLoading(false));
  }, []);

  return (
    <div className="mx-auto max-w-7xl px-6 py-10">
      <h1 className="text-3xl font-bold">Incidents</h1>
      <div className="mt-6 overflow-x-auto rounded-xl border border-slate-200">
        <table className="min-w-full text-sm">
          <thead>
            <tr className="bg-slate-50 text-left">
              <th className="px-4 py-3 font-semibold">ID</th>
              <th className="px-4 py-3 font-semibold">Title</th>
              <th className="px-4 py-3 font-semibold">Severity</th>
              <th className="px-4 py-3 font-semibold">Status</th>
              <th className="px-4 py-3 font-semibold">Asset</th>
              <th className="px-4 py-3 font-semibold">Started</th>
            </tr>
          </thead>
          <tbody>
            {loading ? (
              <tr><td className="px-4 py-3" colSpan={6}>Loading...</td></tr>
            ) : items.length === 0 ? (
              <tr><td className="px-4 py-3" colSpan={6}>No incidents</td></tr>
            ) : (
              items.map((i) => (
                <tr key={i.id} className="border-t">
                  <td className="px-4 py-3">{i.id}</td>
                  <td className="px-4 py-3">{i.title}</td>
                  <td className="px-4 py-3">
                    <span className={`inline-flex items-center rounded-full px-2 py-0.5 text-xs font-medium ${i.severity === 'critical' ? 'bg-red-100 text-red-700' : i.severity === 'high' ? 'bg-orange-100 text-orange-700' : i.severity === 'medium' ? 'bg-yellow-100 text-yellow-700' : 'bg-green-100 text-green-700'}`}>{i.severity}</span>
                  </td>
                  <td className="px-4 py-3">{i.status}</td>
                  <td className="px-4 py-3">{i.asset_id ?? '-'}</td>
                  <td className="px-4 py-3">{i.started_at ? new Date(i.started_at).toLocaleString() : '-'}</td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}
