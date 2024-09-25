from src.application.exceptions import NotFound
from src.application.repositories.sensor_repository import ISensorRepository
from src.application.use_cases.user.base_use_case import BaseUseCase


class UpdateSensorUseCase(BaseUseCase):
    def __init__(self, *, sensor_repository: ISensorRepository):
        self.sensor_repository = sensor_repository

    async def execute(self, *, sensor_id: int, request_data: dict):
        db_sensor = await self.sensor_repository.fetch_one(
            pk=sensor_id
        )
        if not db_sensor:
            raise NotFound

        sensor = await self.sensor_repository.update_one(
            pk=sensor_id,
            data=request_data
        )
        await self.sensor_repository.save_changes()
        return sensor
