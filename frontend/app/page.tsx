"use client";

import { useEffect, useState } from "react";

export default function Dashboard() {
  const [apiInfo, setApiInfo] = useState<any>(null);

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API_BASE}/api/v1`)
      .then((r) => r.json())
      .then(setApiInfo)
      .catch(() => setApiInfo({ error: "API unavailable" }));
  }, []);

  return (
    <div style={{ padding: 24 }}>
      <h1>Sentinel AI Dashboard</h1>
      <p>
        {apiInfo
          ? `Backend: ${apiInfo.name || apiInfo.error} v${apiInfo.version || ''}`
          : "Loading backend info..."}
      </p>
      <div style={{ marginTop: 24 }}>
        <h2>Active Threats</h2>
        <p>Coming soon...</p>
      </div>
    </div>
  );
}
