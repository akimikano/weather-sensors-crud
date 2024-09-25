from abc import ABC, abstractmethod
from typing import TypeVar, Sequence

Entity = TypeVar("Entity")


class AbstractRepository(ABC):

    @abstractmethod
    async def save_one(self, *, entity: Entity):
        ...

    @abstractmethod
    async def save_many(self, *, entity_list: Sequence[Entity]):
        ...

    @abstractmethod
    async def delete_one(self, *, pk: int):
        ...

    @abstractmethod
    async def delete_many(self, *, pk_list: Sequence[int]):
        ...

    @abstractmethod
    async def fetch_many(self, **filters):
        ...

    @abstractmethod
    async def fetch_one(self, *, pk: int, **filters):
        ...

    @abstractmethod
    async def update_one(self, *, pk: int, data: dict):
        ...

    @abstractmethod
    async def update_many(self, *, filters: dict, data: dict):
        ...

    @abstractmethod
    async def save_changes(self):
        ...
