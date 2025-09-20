from __future__ import annotations

from sqlalchemy import String, Integer, ForeignKey, Float
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, TimestampMixin


class Asset(TimestampMixin, Base):
    __tablename__ = "assets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    asset_type: Mapped[str] = mapped_column(String(50), nullable=False)
    ip_address: Mapped[str | None] = mapped_column(String(45), nullable=True)
    cloud_provider: Mapped[str | None] = mapped_column(String(50), nullable=True)
    owner_user_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("users.id"), nullable=True)
    tags: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    risk_score: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)

    owner = relationship("User", back_populates="assets")
    events = relationship("Event", back_populates="asset", cascade="all,delete-orphan")
    incidents = relationship("Incident", back_populates="asset", cascade="all,delete-orphan")
