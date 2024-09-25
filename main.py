import uvicorn

from src.infrastructure.database.sqlalchemy.models import Base
from src.infrastructure.webserver.app import app
from src.infrastructure.webserver.settings import settings
from sqlalchemy import create_engine


def execute():
    engine = create_engine(
        url=f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.POSTGRES_DB}",
        echo=True
    )
    Base.metadata.create_all(engine)

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        access_log=False
    )


if __name__ == "__main__":
    execute()
