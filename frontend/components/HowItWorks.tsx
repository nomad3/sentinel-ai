const steps = [
  { n: 1, title: "Ingest", desc: "Send events via API; data stored in Postgres and indexed in Elasticsearch." },
  { n: 2, title: "Detect", desc: "Anomaly service scores events; rules engine flags critical signals." },
  { n: 3, title: "Respond", desc: "SOAR playbooks enrich, notify, and contain automatically." },
  { n: 4, title: "Report", desc: "Dashboards and APIs provide insights, trends, and auditability." },
];

export default function HowItWorks() {
  return (
    <section className="py-16 bg-slate-50">
      <div className="mx-auto max-w-7xl px-6">
        <h2 className="text-2xl font-semibold text-slate-900">How it works</h2>
        <div className="mt-8 grid gap-6 md:grid-cols-2">
          {steps.map((s) => (
            <div key={s.n} className="rounded-xl border border-slate-200 p-6 bg-white">
              <div className="text-brand-600 font-semibold">{s.n.toString().padStart(2, '0')}</div>
              <h3 className="mt-2 text-lg font-semibold text-slate-900">{s.title}</h3>
              <p className="mt-1 text-slate-600 text-sm">{s.desc}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
