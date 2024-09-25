from enum import Enum


class AuthType(Enum):
    ADMIN = "ADMIN"
    USER = "USER"


class SensorStatus(Enum):
    ACTIVE = "ACTIVE"
    MAINTENANCE = "MAINTENANCE"
    OFFLINE = "OFFLINE"
