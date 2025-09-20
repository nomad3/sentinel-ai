from __future__ import annotations

import os
import httpx
from typing import Optional, Dict, Any


class MISPClient:
    def __init__(self) -> None:
        self.base_url = os.getenv("MISP_URL")
        self.api_key = os.getenv("MISP_API_KEY")
        self.verify_ssl = os.getenv("MISP_VERIFY_SSL", "true").lower() == "true"

    def enabled(self) -> bool:
        return bool(self.base_url and self.api_key)

    def search(self, value: str) -> Optional[Dict[str, Any]]:
        if not self.enabled():
            return None
        headers = {
            "Authorization": self.api_key,
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        try:
            r = httpx.post(
                f"{self.base_url.rstrip('/')}/attributes/restSearch",
                json={"value": value, "limit": 5},
                headers=headers,
                timeout=8,
                verify=self.verify_ssl,
            )
            r.raise_for_status()
            return r.json()
        except Exception:
            return None


misp = MISPClient()
