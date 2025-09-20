from __future__ import annotations

from datetime import datetime

from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.event import Event
from app.models.incident import Incident
from app.search.es import get_client
from app.services import playbooks


def severity_from_score(score: float) -> str:
    if score < 2.0:
        return "low"
    if score < 3.0:
        return "medium"
    if score < 4.0:
        return "high"
    return "critical"


def run_for_event(event_id: int) -> None:
    db: Session = SessionLocal()
    try:
        event = db.get(Event, event_id)
        if event is None:
            return
        if event.anomaly_score is None or event.anomaly_score < 3.0:
            return

        # If already linked to an incident, skip creating a new one
        incident = None
        if event.incident_id:
            incident = db.get(Incident, event.incident_id)

        if incident is None:
            incident = Incident(
                title=f"Anomalous event: {event.event_type}",
                severity=severity_from_score(event.anomaly_score),
                status="open",
                asset_id=event.asset_id,
                started_at=event.occurred_at or datetime.utcnow(),
                description=f"Auto-generated from event {event.id} with score {event.anomaly_score:.2f}",
            )
            db.add(incident)
            db.commit()
            db.refresh(incident)

            event.incident_id = incident.id
            db.add(event)
            db.commit()

            # Index incident in Elasticsearch
            es = get_client()
            es.index(
                index="incidents_v1",
                id=str(incident.id),
                document={
                    "id": str(incident.id),
                    "title": incident.title,
                    "severity": incident.severity,
                    "status": incident.status,
                    "asset_id": incident.asset_id,
                    "started_at": incident.started_at.isoformat() if incident.started_at else None,
                    "resolved_at": incident.resolved_at.isoformat() if incident.resolved_at else None,
                    "created_at": incident.created_at.isoformat() if hasattr(incident, "created_at") else None,
                },
                refresh=False,
            )

        # Run playbooks
        playbooks.enrich(db, incident)
        playbooks.notify(incident)
        if incident.severity == "critical":
            playbooks.contain(db, incident)

    finally:
        db.close()
