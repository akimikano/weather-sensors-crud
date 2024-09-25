from pathlib import Path
from typing import Any, Dict, List, Optional, Union, Callable, Type, Tuple

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = "SECRET_KEY"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    POSTGRES_DB: str = ""
    DB_HOST: str = ""
    DB_PORT: str = ""
    POSTGRES_USER: str = ""
    POSTGRES_PASSWORD: str = ""

    class Config:
        env_file = "./.env"


settings = Settings()
