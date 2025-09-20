from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .core.config import settings
from .api.v1 import api_v1_router
from .db.base import Base
from .db.session import engine
from . import models as _models  # ensure models are imported so tables are created
from .search.es import ensure_indices

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(api_v1_router, prefix="/api/v1")


@app.get("/api/v1")
def api_root():
    return {"name": settings.PROJECT_NAME, "version": settings.VERSION}


@app.on_event("startup")
def on_startup() -> None:
    _ = _models  # reference to avoid linter removing import
    Base.metadata.create_all(bind=engine)
    ensure_indices()
