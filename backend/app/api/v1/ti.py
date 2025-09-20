from __future__ import annotations

from typing import Optional
from fastapi import APIRouter, Query

from app.services.ti_misp import misp
from app.services.ti_virustotal import vt

router = APIRouter()


@router.get("/enrich")
def enrich(value: str = Query(..., description="IP, URL ID, or file hash")):
    result: dict[str, Optional[dict]] = {
        "misp": None,
        "virustotal": None,
    }
    if misp.enabled():
        result["misp"] = misp.search(value)

    if vt.enabled():
        # Heuristic: try IP then file hash then URL id (caller responsible for URL id preprocessing)
        vt_data = vt.ip(value)
        if vt_data is None:
            vt_data = vt.file(value)
        if vt_data is None:
            vt_data = vt.url(value)
        result["virustotal"] = vt_data

    return result
