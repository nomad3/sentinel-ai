export default function CTA() {
  return (
    <section className="py-16 bg-slate-50">
      <div className="mx-auto max-w-7xl px-6 text-center">
        <h3 className="text-2xl font-semibold text-slate-900">Ready to accelerate your SOC?</h3>
        <p className="mt-2 text-slate-600">Spin up locally with Docker and start ingesting events in minutes.</p>
        <div className="mt-6 flex justify-center gap-4">
          <a href="/dashboard" className="rounded-md bg-brand-600 text-white px-6 py-3 font-medium hover:bg-brand-700">Open Dashboard</a>
          <a href="https://github.com/nomad3/sentinel-ai" target="_blank" rel="noreferrer" className="rounded-md border border-slate-300 px-6 py-3 font-medium text-slate-700 hover:bg-slate-100">View on GitHub</a>
        </div>
      </div>
    </section>
  );
}
