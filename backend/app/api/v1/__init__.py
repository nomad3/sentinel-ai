from fastapi import APIRouter

from .health import router as health
from .ingest import router as ingest
from .anomaly import router as anomaly
from .incidents import router as incidents
from .ti import router as ti

api_v1_router = APIRouter()
api_v1_router.include_router(health, prefix="/health", tags=["health"])
api_v1_router.include_router(ingest, prefix="/ingest", tags=["ingest"])
api_v1_router.include_router(anomaly, prefix="/anomaly", tags=["anomaly"])
api_v1_router.include_router(incidents, prefix="/incidents", tags=["incidents"])
api_v1_router.include_router(ti, prefix="/ti", tags=["threat-intel"])
