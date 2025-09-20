"use client";

import { useEffect, useState } from "react";

export default function Dashboard() {
  const [apiInfo, setApiInfo] = useState<any>(null);

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API_BASE}/api/v1`)
      .then((r) => r.json())
      .then(setApiInfo)
      .catch(() => setApiInfo({ error: "API unavailable" }));
  }, []);

  return (
    <div className="mx-auto max-w-7xl px-6 py-10">
      <h1 className="text-3xl font-bold">Dashboard</h1>
      <p className="mt-2 text-slate-600">
        {apiInfo ? `Backend: ${apiInfo.name || apiInfo.error} v${apiInfo.version || ''}` : "Loading backend info..."}
      </p>
      <div className="mt-8 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
        <div className="rounded-xl border border-slate-200 p-6">
          <h3 className="font-semibold">Active Threats</h3>
          <p className="text-sm text-slate-600 mt-2">Coming soon...</p>
        </div>
        <div className="rounded-xl border border-slate-200 p-6">
          <h3 className="font-semibold">Recent Incidents</h3>
          <p className="text-sm text-slate-600 mt-2">Coming soon...</p>
        </div>
        <div className="rounded-xl border border-slate-200 p-6">
          <h3 className="font-semibold">Risk Score</h3>
          <p className="text-sm text-slate-600 mt-2">Coming soon...</p>
        </div>
      </div>
    </div>
  );
}
