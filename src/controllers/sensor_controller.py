from typing import TypeAlias, Annotated

from fastapi import Depends

from src.application.use_cases.sensor.create_sensor import CreateSensorUseCase
from src.application.use_cases.sensor.delete_sensor import DeleteSensorUseCase
from src.application.use_cases.sensor.fetch_sensor import FetchSensorUseCase
from src.application.use_cases.sensor.fetch_sensors import FetchSensorsUseCase
from src.application.use_cases.sensor.update_sensor import UpdateSensorUseCase
from src.infrastructure.database.sqlalchemy.config import get_db_session

from src.infrastructure.database.sqlalchemy.repositories.sensor_repository import \
    SensorRepository


class SensorController:
    def __init__(
        self,
        db_connection=Depends(get_db_session)
    ):
        self.sensor_repository = SensorRepository(
            db_connection=db_connection
        )

    async def fetch_sensors(self):
        fetch_sensors_use_case = FetchSensorsUseCase(
            sensor_repository=self.sensor_repository
        )
        return await fetch_sensors_use_case.execute()

    async def fetch_sensor(self, *, sensor_id: int):
        fetch_sensor_use_case = FetchSensorUseCase(
            sensor_repository=self.sensor_repository
        )
        return await fetch_sensor_use_case.execute(sensor_id=sensor_id)

    async def create_sensor(self, *, request_data: dict):
        create_sensor_use_case = CreateSensorUseCase(
            sensor_repository=self.sensor_repository
        )
        return await create_sensor_use_case.execute(request_data=request_data)

    async def update_sensor(self, *, sensor_id: int, request_data: dict):
        update_sensor_use_case = UpdateSensorUseCase(
            sensor_repository=self.sensor_repository
        )
        return await update_sensor_use_case.execute(
            sensor_id=sensor_id,
            request_data=request_data
        )

    async def delete_sensor(self, *, sensor_id: int):
        delete_sensor_use_case = DeleteSensorUseCase(
            sensor_repository=self.sensor_repository
        )
        return await delete_sensor_use_case.execute(sensor_id=sensor_id)


SensorControllerDep: TypeAlias = Annotated[SensorController, Depends(SensorController)]
