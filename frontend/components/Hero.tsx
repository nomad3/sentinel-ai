export default function Hero() {
  return (
    <section className="bg-gradient-to-b from-brand-50 to-white">
      <div className="mx-auto max-w-7xl px-6 py-16 text-center">
        <h1 className="text-4xl md:text-6xl font-bold tracking-tight text-slate-900">
          AI-Driven Cyber Defense
        </h1>
        <p className="mt-6 text-lg text-slate-600 max-w-2xl mx-auto">
          Real-time threat detection, automated response, and decision support
          built for modern cloud and enterprise environments.
        </p>
        <div className="mt-8 flex justify-center gap-4">
          <a href="/dashboard" className="rounded-md bg-brand-600 text-white px-6 py-3 font-medium hover:bg-brand-700">Open Dashboard</a>
          <a href="/api/docs" className="rounded-md border border-slate-300 px-6 py-3 font-medium text-slate-700 hover:bg-slate-50">API Docs</a>
        </div>
      </div>
    </section>
  );
}
