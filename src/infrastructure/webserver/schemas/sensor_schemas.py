from datetime import datetime

from pydantic import BaseModel

from src.domain.enums import SensorStatus


class SensorBase(BaseModel):
    sensor_model: str
    location: str
    installed_at: datetime
    device_status: SensorStatus


class SensorCreate(SensorBase):
    pass


class SensorUpdate(SensorBase):
    pass


class SensorDetail(SensorBase):
    id: int
