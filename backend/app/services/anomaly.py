from __future__ import annotations

from datetime import datetime
from typing import List, Optional

import numpy as np
from sklearn.ensemble import IsolationForest

from app.models.event import Event


class AnomalyDetector:
    def __init__(self) -> None:
        self.model: Optional[IsolationForest] = None
        self.fitted: bool = False

    def _extract_features_from_event(self, event: Event) -> np.ndarray:
        source_hash = hash(event.source) % 1000 if event.source else 0
        type_hash = hash(event.event_type) % 1000 if event.event_type else 0
        raw_len = len(event.raw) if isinstance(event.raw, dict) else 0
        asset_flag = 1 if event.asset_id else 0
        hour = event.occurred_at.hour if isinstance(event.occurred_at, datetime) else 0
        return np.array([source_hash, type_hash, raw_len, asset_flag, hour], dtype=float)

    def fit(self, events: List[Event]) -> None:
        if not events:
            self.model = None
            self.fitted = False
            return
        X = np.vstack([self._extract_features_from_event(e) for e in events])
        # Scale simple features roughly to stabilize IF behavior
        # Avoid complex preprocessing for MVP
        X[:, 0:2] = X[:, 0:2] / 1000.0
        X[:, 2] = np.log1p(X[:, 2])
        X[:, 4] = X[:, 4] / 24.0
        self.model = IsolationForest(n_estimators=100, contamination="auto", random_state=42)
        self.model.fit(X)
        self.fitted = True

    def score(self, event: Event) -> Optional[float]:
        if not self.model or not self.fitted:
            return None
        x = self._extract_features_from_event(event)
        x[0:2] = x[0:2] / 1000.0
        x[2] = np.log1p(x[2])
        x[4] = x[4] / 24.0
        score = -float(self.model.score_samples([x])[0])
        # Higher is more anomalous after negating score_samples
        return score


anomaly_detector = AnomalyDetector()
