from src.application.repositories.sensor_repository import ISensorRepository
from src.domain.entities.sensor import SensorEntity
from src.infrastructure.database.sqlalchemy.models import SensorModel
from src.infrastructure.database.sqlalchemy.repositories.base_repository import \
    BaseAsyncRepository


class SensorRepository(BaseAsyncRepository, ISensorRepository):
    model = SensorModel

    @staticmethod
    def to_entity(db_instance: SensorModel):
        return SensorEntity(
            id=db_instance.id,
            sensor_model=db_instance.sensor_model,
            location=db_instance.location,
            installed_at=db_instance.installed_at,
            device_status=db_instance.device_status
        )
