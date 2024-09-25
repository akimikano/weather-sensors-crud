from src.application.repositories.sensor_repository import ISensorRepository
from src.application.use_cases.user.base_use_case import BaseUseCase


class FetchSensorsUseCase(BaseUseCase):
    def __init__(self, *, sensor_repository: ISensorRepository):
        self.sensor_repository = sensor_repository

    async def execute(self):
        return await self.sensor_repository.fetch_many()
