from src.application.repositories.sensor_repository import ISensorRepository
from src.application.use_cases.user.base_use_case import BaseUseCase


class DeleteSensorUseCase(BaseUseCase):
    def __init__(self, *, sensor_repository: ISensorRepository):
        self.sensor_repository = sensor_repository

    async def execute(self, *, sensor_id: int):
        await self.sensor_repository.delete_one(pk=sensor_id)
        await self.sensor_repository.save_changes()
