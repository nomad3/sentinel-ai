const integrations = [
  { name: "Elasticsearch", href: "http://localhost:5601" },
  { name: "PostgreSQL", href: "#" },
  { name: "MISP", href: "#" },
  { name: "VirusTotal", href: "#" },
  { name: "Slack", href: "#" },
];

export default function Integrations() {
  return (
    <section className="py-16">
      <div className="mx-auto max-w-7xl px-6">
        <h2 className="text-2xl font-semibold text-slate-900">Integrations</h2>
        <div className="mt-6 grid gap-4 grid-cols-2 sm:grid-cols-3 md:grid-cols-5">
          {integrations.map((i) => (
            <a key={i.name} href={i.href} className="rounded-lg border border-slate-200 px-4 py-6 text-center hover:border-brand-300">
              <span className="font-semibold text-slate-800">{i.name}</span>
            </a>
          ))}
        </div>
      </div>
    </section>
  );
}
