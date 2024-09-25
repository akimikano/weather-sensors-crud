from typing import List

from fastapi import APIRouter
from fastapi import status

from src.controllers.sensor_controller import SensorControllerDep
from src.infrastructure.webserver.dependencies import IntPath
from src.infrastructure.authentication.jwt_authentication import UserSession
from src.infrastructure.webserver.schemas.sensor_schemas import SensorDetail, \
    SensorCreate

router = APIRouter()


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[SensorDetail]
)
async def get_sensors(
    sensor_controller: SensorControllerDep,
    user: UserSession, # noqa
):
    return await sensor_controller.fetch_sensors()


@router.get(
    "/{sensor_id}",
    status_code=status.HTTP_200_OK,
    response_model=EquipmentDetail
)
async def get_sensor(
    sensor_controller: SensorControllerDep,
    sensor_id: IntPath,
    user: UserSession # noqa
):
    return await sensor_controller.fetch_sensor(sensor_id=sensor_id)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=SensorDetail
)
async def create_sensor(
    sensor_controller: SensorControllerDep,
    user: UserSession, # noqa
    request_data: SensorCreate
):
    return await sensor_controller.create_sensor(
        request_data=request_data.dict()
    )


@router.put(
    "/{sensor_id}",
    status_code=status.HTTP_200_OK,
    response_model=SensorDetail
)
async def update_sensor(
    sensor_controller: SensorControllerDep,
    user: UserSession, # noqa
    sensor_id: IntPath,
    request_data: SensorCreate
):
    return await sensor_controller.update_sensor(
        sensor_id=sensor_id,
        request_data=request_data.dict()
    )


@router.delete(
    "/{sensor_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_sensor(
    sensor_controller: SensorControllerDep,
    user: UserSession, # noqa
    sensor_id: IntPath,
):
    return await sensor_controller.delete_sensor(
        sensor_id=sensor_id,
    )
