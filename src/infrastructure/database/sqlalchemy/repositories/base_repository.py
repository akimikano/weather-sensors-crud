from typing import TypeVar, Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc, inspect, update, literal_column, delete

from src.application.repositories.abstract_repository import AbstractRepository
from src.domain.entities.user import UserEntity

Entity = TypeVar("Entity")
DbModel = TypeVar("DbModel")
DbConnection = TypeVar("DbConnection", bound=AsyncSession)


class BaseAsyncRepository(AbstractRepository):
    model: DbModel

    def __init__(self, db_connection: DbConnection):
        self.db_connection = db_connection

    async def save_one(self, *, entity: Entity):
        db_model = self.model(**entity.__dict__)
        self.db_connection.add(db_model)
        await self.db_connection.flush()

        entity.id = db_model.id
        return entity

    async def save_many(self, *, entity_list: Sequence[Entity]):
        for entity in entity_list:
            await self.save_one(entity=entity)

        return entity_list

    async def delete_one(self, *, pk: int):
        query = (
            delete(self.model)
            .where(self.model.id == pk))

        await self.db_connection.execute(query)
        await self.db_connection.flush()

    async def delete_many(self, *, pk_list: Sequence[int]):
        pass

    @staticmethod
    def to_entity(db_instance: DbModel):
        return None

    def query(self):
        return select(self.model).order_by(desc(self.model.id))

    async def fetch_many(self, **filters):
        query = self.query()
        result = await self.db_connection.execute(query)
        db_instances = result.scalars().all()
        return [self.to_entity(db_instance) for db_instance in db_instances]

    async def fetch_one(self, *, pk: int, **filters):
        query = self.query()
        query = query.filter(self.model.id == pk)
        result = await self.db_connection.execute(query)
        db_instance = result.scalar_one_or_none()
        return self.to_entity(db_instance=db_instance)

    async def update_one(self, *, pk: int, data: dict):
        query = (
            update(self.model)
            .where(self.model.id == pk)
            .values(**data)
            .returning(self.model)
        )

        result = await self.db_connection.execute(query)
        await self.db_connection.flush()
        return self.to_entity(db_instance=result.scalar_one_or_none())

    async def update_many(self, *, filters: dict, data: dict):
        pass

    async def save_changes(self):
        await self.db_connection.commit()
