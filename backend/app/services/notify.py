from __future__ import annotations

import os
import json
import httpx


class Notifier:
    def __init__(self) -> None:
        self.slack_webhook = os.getenv("SLACK_WEBHOOK_URL")

    def send(self, title: str, text: str) -> None:
        if self.slack_webhook:
            payload = {"text": f"*{title}*\n{text}"}
            try:
                httpx.post(self.slack_webhook, headers={"Content-Type": "application/json"}, content=json.dumps(payload), timeout=5)
                return
            except Exception:
                pass
        # Fallback: stdout
        print(f"NOTIFY: {title}\n{text}")


notifier = Notifier()
