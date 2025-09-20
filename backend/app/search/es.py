from __future__ import annotations

from typing import Optional
from elasticsearch import Elasticsearch

from app.core.config import settings

_es_client: Optional[Elasticsearch] = None


def get_client() -> Elasticsearch:
    global _es_client
    if _es_client is None:
        _es_client = Elasticsearch(settings.ELASTICSEARCH_URL)
    return _es_client


def ensure_indices() -> None:
    es = get_client()

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
        if not es.indices.exists(index=index_name):
            es.indices.create(index=index_name, **body)
