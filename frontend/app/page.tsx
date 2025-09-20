"use client";

import CTA from "@/components/CTA";
import Features from "@/components/Features";
import Footer from "@/components/Footer";
import Hero from "@/components/Hero";
import HowItWorks from "@/components/HowItWorks";
import Integrations from "@/components/Integrations";
import LiveIncidents from "@/components/LiveIncidents";
import Navbar from "@/components/Navbar";
import Testimonials from "@/components/Testimonials";

export default function Landing() {
  return (
    <div className="flex min-h-screen flex-col">
      <Navbar />
      <main className="flex-1">
        <Hero />
        <Features />
        <HowItWorks />
        <Integrations />
        <LiveIncidents />
        <Testimonials />
        <CTA />
      </main>
      <Footer />
    </div>
  );
}
