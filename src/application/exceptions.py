from typing import Optional


class ApplicationException(Exception):
    default_message = ""

    def __init__(self, message: Optional[str] = None):
        self.message = message or self.default_message


class UserWithEmailExists(ApplicationException):
    default_message = "User with such email already exists."


class NotFound(ApplicationException):
    default_message = "NotFound."

