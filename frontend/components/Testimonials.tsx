const quotes = [
  {
    name: "SOC Lead, FinTech",
    text: "Sentinel AI helped us cut response times dramatically during our cloud migration.",
  },
  {
    name: "CISO, SaaS",
    text: "The automated playbooks and anomaly scoring give us 24/7 confidence.",
  },
];

export default function Testimonials() {
  return (
    <section className="py-16 bg-white">
      <div className="mx-auto max-w-7xl px-6">
        <h2 className="text-2xl font-semibold text-slate-900">What users say</h2>
        <div className="mt-8 grid gap-6 md:grid-cols-2">
          {quotes.map((q) => (
            <figure key={q.name} className="rounded-xl border border-slate-200 p-6 bg-slate-50">
              <blockquote className="text-slate-700">“{q.text}”</blockquote>
              <figcaption className="mt-2 text-sm text-slate-500">— {q.name}</figcaption>
            </figure>
          ))}
        </div>
      </div>
    </section>
  );
}
