from __future__ import annotations

import os
from typing import Optional, Dict, Any
import httpx


class VirusTotalClient:
    def __init__(self) -> None:
        self.api_key = os.getenv("VT_API_KEY")

    def enabled(self) -> bool:
        return bool(self.api_key)

    def _get(self, path: str) -> Optional[Dict[str, Any]]:
        if not self.enabled():
            return None
        headers = {"x-apikey": self.api_key}
        try:
            r = httpx.get(f"https://www.virustotal.com/api/v3/{path}", headers=headers, timeout=8)
            r.raise_for_status()
            return r.json()
        except Exception:
            return None

    def ip(self, ip_address: str) -> Optional[Dict[str, Any]]:
        return self._get(f"ip_addresses/{ip_address}")

    def url(self, url_id: str) -> Optional[Dict[str, Any]]:
        return self._get(f"urls/{url_id}")

    def file(self, hash_id: str) -> Optional[Dict[str, Any]]:
        return self._get(f"files/{hash_id}")


vt = VirusTotalClient()
