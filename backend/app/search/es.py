from __future__ import annotations

from typing import Optional
from time import sleep, time
from elasticsearch import Elasticsearch

from app.core.config import settings

_es_client: Optional[Elasticsearch] = None


def get_client() -> Elasticsearch:
    global _es_client
    if _es_client is None:
        _es_client = Elasticsearch(settings.ELASTICSEARCH_URL)
    return _es_client


def wait_for_ready(timeout_seconds: int = 90, interval_seconds: float = 2.0) -> None:
    es = get_client()
    start = time()
    while time() - start < timeout_seconds:
        try:
            if es.ping():
                return
        except Exception:
            pass
        sleep(interval_seconds)
    raise RuntimeError("Elasticsearch not ready within timeout")


def ensure_indices() -> None:
    es = get_client()

    # Wait until cluster is reachable
    try:
        wait_for_ready()
    except Exception:
        # Best-effort: continue and let index operations fail noisily
        pass

    indices = {
        "events_v1": {
            "mappings": {
                "properties": {
                    "id": {"type": "keyword"},
                    "source": {"type": "keyword"},
                    "event_type": {"type": "keyword"},
                    "asset_id": {"type": "long"},
                    "incident_id": {"type": "long"},
                    "occurred_at": {"type": "date"},
                    "anomaly_score": {"type": "float"},
                    "raw": {"type": "object", "enabled": True},
                    "created_at": {"type": "date"},
                }
            }
        },
        "incidents_v1": {
            "mappings": {
                "properties": {
                    "id": {"type": "keyword"},
                    "title": {"type": "text"},
                    "severity": {"type": "keyword"},
                    "status": {"type": "keyword"},
                    "asset_id": {"type": "long"},
                    "started_at": {"type": "date"},
                    "resolved_at": {"type": "date"},
                    "created_at": {"type": "date"},
                }
            }
        },
        "assets_v1": {
            "mappings": {
                "properties": {
                    "id": {"type": "keyword"},
                    "name": {"type": "text"},
                    "asset_type": {"type": "keyword"},
                    "ip_address": {"type": "ip"},
                    "cloud_provider": {"type": "keyword"},
                    "risk_score": {"type": "float"},
                    "tags": {"type": "object"},
                    "created_at": {"type": "date"},
                }
            }
        },
    }

    for index_name, body in indices.items():
        try:
            if not es.indices.exists(index=index_name):
                es.indices.create(index=index_name, **body)
        except Exception:
            # Ignore index creation races or transient errors
            pass
