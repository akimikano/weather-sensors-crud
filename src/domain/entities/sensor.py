from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List


@dataclass
class SensorEntity:
    id: Optional[int]
    sensor_model: str
    location: str
    installed_at: datetime
    device_status: str
