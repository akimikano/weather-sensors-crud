from abc import ABC, abstractmethod

from src.application.repositories.abstract_repository import AbstractRepository


class IUserRepository(AbstractRepository, ABC):

    @abstractmethod
    async def fetch_by_email(self, *, email: str):
        ...
