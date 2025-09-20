from __future__ import annotations

from datetime import datetime
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models import Event
from app.search.es import get_client
from app.services.anomaly import anomaly_detector
from app.services.soar import run_for_event

router = APIRouter()


class IngestEvent(BaseModel):
    source: str = Field(..., examples=["aws-cloudtrail", "syslog"])
    event_type: str
    asset_id: int | None = None
    occurred_at: datetime | None = None
    raw: dict | None = None


def index_event_es(event: Event) -> None:
    es = get_client()
    es.index(
        index="events_v1",
        id=str(event.id),
        document={
            "id": str(event.id),
            "source": event.source,
            "event_type": event.event_type,
            "asset_id": event.asset_id,
            "incident_id": event.incident_id,
            "occurred_at": event.occurred_at.isoformat() if event.occurred_at else None,
            "anomaly_score": event.anomaly_score,
            "raw": event.raw,
            "created_at": event.created_at.isoformat() if hasattr(event, "created_at") else None,
        },
        refresh=False,
    )


@router.post("/events", status_code=202)
def ingest_event(payload: IngestEvent, background: BackgroundTasks, db: Session = Depends(get_db)):
    event = Event(
        source=payload.source,
        event_type=payload.event_type,
        asset_id=payload.asset_id,
        occurred_at=payload.occurred_at,
        raw=payload.raw,
    )

    # Compute anomaly score if model fitted
    score = anomaly_detector.score(event)
    if score is not None:
        event.anomaly_score = score

    db.add(event)
    db.commit()
    db.refresh(event)

    background.add_task(index_event_es, event)
    background.add_task(run_for_event, event.id)

    return {"id": event.id, "status": "accepted", "anomaly_score": event.anomaly_score}
