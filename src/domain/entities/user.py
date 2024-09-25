from dataclasses import dataclass
from typing import Optional


@dataclass
class UserEntity:
    id: Optional[int]
    first_name: str
    last_name: str
    email: str
    auth_type: str
    password_hash: str
