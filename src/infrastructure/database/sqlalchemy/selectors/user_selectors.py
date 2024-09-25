from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.infrastructure.database.sqlalchemy.models import UserModel


async def get_user(db_connection: AsyncSession, email: str):
    query = select(UserModel).filter(UserModel.email == email)
    result = await db_connection.execute(query)
    return result.scalar_one_or_none()
