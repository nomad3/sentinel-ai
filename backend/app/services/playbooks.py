from __future__ import annotations

from datetime import datetime
from sqlalchemy.orm import Session

from app.models.incident import Incident
from app.services.notify import notifier


def notify(incident: Incident) -> None:
    title = f"Incident #{incident.id}: {incident.title} ({incident.severity})"
    text = f"Status: {incident.status}\nAsset: {incident.asset_id}\nStarted: {incident.started_at}"
    try:
        notifier.send(title, text)
    except Exception:
        # Best-effort; do not raise in playbooks
        pass


def enrich(db: Session, incident: Incident) -> None:
    # Placeholder enrichment - append a note to description
    note = f"[Enriched at {datetime.utcnow().isoformat()}Z]"
    if incident.description:
        incident.description += f"\n{note}"
    else:
        incident.description = note
    db.add(incident)
    db.commit()


def contain(db: Session, incident: Incident) -> None:
    # Simple containment: mark status to contained for critical incidents
    if incident.severity.lower() == "critical" and incident.status != "contained":
        incident.status = "contained"
        db.add(incident)
        db.commit()
