from __future__ import annotations

from typing import Optional
from fastapi import APIRouter, Depends, BackgroundTasks
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.event import Event
from app.services.anomaly import anomaly_detector

router = APIRouter()


class RetrainParams(BaseModel):
    limit: int = 2000


def _do_retrain(db: Session, limit: int) -> None:
    events = db.query(Event).order_by(Event.created_at.desc()).limit(limit).all()
    anomaly_detector.fit(list(reversed(events)))


@router.post("/retrain")
def retrain(params: RetrainParams, background: BackgroundTasks, db: Session = Depends(get_db)):
    background.add_task(_do_retrain, db, params.limit)
    return {"status": "training_scheduled", "limit": params.limit}


@router.get("/status")
def status():
    return {"fitted": anomaly_detector.fitted}
