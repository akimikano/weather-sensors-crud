from abc import ABC, abstractmethod


class AbstractUseCase(ABC):
    @abstractmethod
    async def execute(self):
        ...
