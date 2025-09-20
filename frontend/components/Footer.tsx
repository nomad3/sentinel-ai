export default function Footer() {
  return (
    <footer className="border-t border-slate-200 mt-20">
      <div className="mx-auto max-w-7xl px-6 py-8 text-sm text-slate-500 grid gap-4 md:flex items-center justify-between">
        <p>© {new Date().getFullYear()} Sentinel AI</p>
        <div className="flex gap-4">
          <a href="/api/docs" className="hover:text-brand-600">API Docs</a>
          <a href="https://github.com/nomad3/sentinel-ai" className="hover:text-brand-600" target="_blank" rel="noreferrer">GitHub</a>
          <a href="/dashboard" className="hover:text-brand-600">Dashboard</a>
        </div>
      </div>
    </footer>
  );
}
