from pydantic import BaseModel, EmailStr, Field, ConfigDict

from src.domain.enums import AuthType


PasswordStr = Field(min_length=8, max_length=64)


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    auth_type: AuthType


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    pass


class UserDetail(UserBase):
    id: int


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserRegister(BaseModel):
    model_config = ConfigDict(extra="allow")

    first_name: str
    last_name: str
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
