from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Text, Enum

from src.domain.enums import AuthType
from src.infrastructure.database.sqlalchemy.models.base_model import Base


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(255))
    last_name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255))
    auth_type: Mapped[str] = mapped_column(Enum(AuthType), default=AuthType.USER)
    password_hash: Mapped[str] = mapped_column(Text)
