from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, Enum

from src.domain.enums import SensorStatus
from src.infrastructure.database.sqlalchemy.models.base_model import Base


class SensorModel(Base):
    __tablename__ = "sensors"

    id: Mapped[int] = mapped_column(primary_key=True)
    sensor_model: Mapped[str] = mapped_column(String(255))
    location: Mapped[str] = mapped_column(String(255))
    installed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    device_status: Mapped[str] = mapped_column(Enum(SensorStatus))
