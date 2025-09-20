const features = [
  { title: "Real-Time Detection", desc: "Stream, analyze, and score events at scale using AI." },
  { title: "SOAR Automation", desc: "Respond faster with playbooks for notify, enrich, contain." },
  { title: "Threat Intel", desc: "Contextual enrichment via MISP and VirusTotal connectors." },
  { title: "Dashboards", desc: "Operational and executive views with search and charts." },
  { title: "Scalable", desc: "Cloud-native stack on Docker/K8s, ready to scale." },
  { title: "Secure", desc: "DevSecOps with CI scans, RBAC (coming), and audit logs." },
];

export default function Features() {
  return (
    <section className="py-16">
      <div className="mx-auto max-w-7xl px-6">
        <h2 className="text-2xl font-semibold text-slate-900">Why Sentinel AI</h2>
        <div className="mt-8 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {features.map((f) => (
            <div key={f.title} className="rounded-xl border border-slate-200 p-6 bg-white shadow-sm">
              <h3 className="font-semibold text-slate-900">{f.title}</h3>
              <p className="mt-2 text-slate-600 text-sm">{f.desc}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
