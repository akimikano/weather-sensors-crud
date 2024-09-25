from src.application.repositories.sensor_repository import ISensorRepository
from src.application.use_cases.user.base_use_case import BaseUseCase
from src.domain.entities.sensor import SensorEntity


class CreateSensorUseCase(BaseUseCase):
    def __init__(self, *, sensor_repository: ISensorRepository):
        self.sensor_repository = sensor_repository

    async def execute(self, request_data: dict):
        sensor = SensorEntity(
            id=None,
            **request_data
        )

        await self.sensor_repository.save_one(entity=sensor)
        await self.sensor_repository.save_changes()
        return sensor
