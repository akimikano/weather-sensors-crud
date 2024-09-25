from typing import AsyncGenerator, TypeAlias, Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from src.infrastructure.webserver.settings import settings

engine = create_async_engine(
    url=f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.POSTGRES_DB}",
    echo=True
)


async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)


async def get_db_session() -> AsyncGenerator:
    async with async_session() as session:
        yield session


DbSession: TypeAlias = Annotated[AsyncSession, Depends(get_db_session)]
