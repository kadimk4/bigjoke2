import msgspec
from uuid import UUID

class CreateUserCommand(msgspec.Struct):
    tg_id: int | None = None
    username: str

class UpdateUserCommand(msgspec.Struct):
    uuid: UUID
    username: str | None = None
    tg_id: int | None = None

class GetUserByIdQuery(msgspec.Struct):
    uuid: UUID

class GetUserByTgQuery(msgspec.Struct):
    tg_id: int

class UserResponseDTO(msgspec.Struct):
    uuid: UUID
    tg_id: int | None
    username: str
    role: str