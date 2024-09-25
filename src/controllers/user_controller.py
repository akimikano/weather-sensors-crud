from typing import TypeAlias, Annotated

from fastapi import Depends

from src.application.use_cases.user.create_user import CreateUserUseCase
from src.domain.entities.user import UserEntity
from src.infrastructure.database.sqlalchemy.config import get_db_session
from src.infrastructure.database.sqlalchemy.repositories.user_repository import \
    UserRepository


class UserController:
    def __init__(
        self,
        db_connection=Depends(get_db_session)
    ):
        self.user_repository = UserRepository(db_connection=db_connection)

    async def create_user(self, request_data: dict):
        create_user_use_case = CreateUserUseCase(
            user_repository=self.user_repository
        )
        return await create_user_use_case.execute(request_data=request_data)

    async def fetch_users(self):
        return await self.user_repository.fetch_many()

    async def fetch_user(self, *, user_id: int):
        return await self.user_repository.fetch_one(pk=user_id)

    async def update_user(self, *, user_id: int, data: dict):
        user = await self.user_repository.update_one(pk=user_id, data=data)
        await self.user_repository.save_changes()
        return user

    async def delete_user(self, *, user_id: int):
        await self.user_repository.delete_one(pk=user_id)
        await self.user_repository.save_changes()

    async def create_jwt_token(self):
        pass


UserControllerDep: TypeAlias = Annotated[UserController, Depends(UserController)]
