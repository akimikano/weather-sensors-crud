from datetime import datetime, timedelta, timezone
from typing import Annotated, TypeAlias

import jwt
from fastapi import Depends, HTTPException, status, Header
from jwt.exceptions import InvalidTokenError
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.enums import AuthType
from src.domain.services.auth import verify_password
from src.infrastructure.database.sqlalchemy.config import get_db_session, \
    DbSession
from src.infrastructure.database.sqlalchemy.models import UserModel
from src.infrastructure.webserver.schemas.user_schemas import Token
from src.infrastructure.webserver.settings import settings
from src.infrastructure.database.sqlalchemy.selectors.user_selectors import \
    get_user


class JWTAuthentication:
    def __init__(self, *, db_connection: DbSession):
        self.db_connection = db_connection

    async def authenticate_user(
            self,
            *,
            email: str,
            password: str
    ):
        user = await get_user(db_connection=self.db_connection, email=email)

        if not user:
            return False

        if not verify_password(password, user.password_hash):
            return False

        return user

    @staticmethod
    def create_access_token(
            *,
            data: dict,
            expires_delta: timedelta | None = None
    ):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode,
            settings.SECRET_KEY,
            algorithm=settings.ALGORITHM
        )
        return encoded_jwt

    async def get_current_user(
            self,
            *,
            token: Annotated[str, Header(...)]
    ):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(
                token,
                settings.SECRET_KEY,
                algorithms=[settings.ALGORITHM]
            )
            user_email = payload.get("sub")
            if user_email is None:
                raise credentials_exception

        except InvalidTokenError:
            raise credentials_exception

        user = await get_user(db_connection=self.db_connection, email=user_email)

        if user is None:
            raise credentials_exception
        return user

    async def authenticate(self, *, email: str, password: str):
        user = await self.authenticate_user(email=email, password=password)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        access_token_expires = timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

        access_token = self.create_access_token(
            data={"sub": email},
            expires_delta=access_token_expires
        )

        return Token(access_token=access_token, token_type="bearer")


async def get_user_session(
    db_connection: DbSession,
    token: Annotated[str, Header(...)]
):
    jwt_authentication = JWTAuthentication(db_connection=db_connection)
    return await jwt_authentication.get_current_user(token=token)


async def get_admin_session(
    db_connection: DbSession,
    token: Annotated[str, Header(...)]
):
    user = await get_user_session(db_connection=db_connection, token=token)

    if user.auth_type != AuthType.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not permitted.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


JWTAuthenticationDep: TypeAlias = Annotated[JWTAuthentication, Depends(JWTAuthentication)]
UserSession: TypeAlias = Annotated[UserModel, Depends(get_user_session)]
AdminSession: TypeAlias = Annotated[UserModel, Depends(get_admin_session)]
