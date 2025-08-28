from dataclasses import dataclass


@dataclass(frozen=True)
class BaseUserException(Exception):
    @property
    def message(self):
        return "Something wrong"


@dataclass(eq=False)
class UsernameException(BaseUserException):
    @property
    def message(self):
        return "Username too short/long or contains incorrect charters"
