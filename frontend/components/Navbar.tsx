"use client";

import Link from "next/link";
import { useState } from "react";

export default function Navbar() {
  const [open, setOpen] = useState(false);
  return (
    <header className="border-b border-slate-200">
      <div className="mx-auto max-w-7xl px-6 py-4 flex items-center justify-between">
        <Link href="/" className="font-bold text-xl text-brand-700">Sentinel AI</Link>
        <button className="md:hidden" onClick={() => setOpen(!open)} aria-label="Menu">
          <svg className="h-6 w-6" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
        </button>
        <nav className={`md:flex gap-6 items-center ${open ? 'block' : 'hidden'} md:block`}>
          <Link href="/dashboard" className="text-slate-700 hover:text-brand-600">Dashboard</Link>
          <Link href="/admin/overview" className="text-slate-700 hover:text-brand-600">Admin</Link>
          <Link href="/admin/incidents" className="text-slate-700 hover:text-brand-600">Incidents</Link>
          <a href="/api/docs" className="text-slate-700 hover:text-brand-600">API</a>
        </nav>
      </div>
    </header>
  );
}
