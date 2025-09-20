export default function AdminOverview() {
  return (
    <div className="mx-auto max-w-7xl px-6 py-10">
      <h1 className="text-3xl font-bold">Admin Overview</h1>
      <div className="mt-8 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
        {["Events Today", "Incidents", "Critical", "Avg Score"].map((t) => (
          <div key={t} className="rounded-xl border border-slate-200 p-6">
            <div className="text-sm text-slate-500">{t}</div>
            <div className="text-2xl font-semibold mt-2">--</div>
          </div>
        ))}
      </div>
      <div className="mt-10 rounded-xl border border-slate-200 p-6">
        <h2 className="font-semibold">Trends</h2>
        <p className="text-sm text-slate-600 mt-2">Charts coming soon...</p>
      </div>
    </div>
  );
}
