from __future__ import annotations

from typing import List, Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.incident import Incident

router = APIRouter()


@router.get("/", response_model=list[dict])
def list_incidents(status: Optional[str] = None, limit: int = 50, db: Session = Depends(get_db)):
    q = db.query(Incident).order_by(Incident.created_at.desc())
    if status:
        q = q.filter(Incident.status == status)
    q = q.limit(min(limit, 200))
    items: List[Incident] = q.all()
    return [
        {
            "id": i.id,
            "title": i.title,
            "severity": i.severity,
            "status": i.status,
            "asset_id": i.asset_id,
            "started_at": i.started_at,
            "resolved_at": i.resolved_at,
            "created_at": i.created_at,
        }
        for i in items
    ]


@router.get("/{incident_id}", response_model=dict)
def get_incident(incident_id: int, db: Session = Depends(get_db)):
    i: Optional[Incident] = db.get(Incident, incident_id)
    if not i:
        return {}
    return {
        "id": i.id,
        "title": i.title,
        "severity": i.severity,
        "status": i.status,
        "asset_id": i.asset_id,
        "started_at": i.started_at,
        "resolved_at": i.resolved_at,
        "description": i.description,
        "created_at": i.created_at,
    }
