from dataclasses import dataclass, field
from uuid import uuid4, UUID
from enum import Enum
from src.app.domain.users.exceptions import UsernameException
class BaseUserRoles(Enum):
    MEMBER = 'member'
    CREATOR = 'creator'
    ADMIN = 'admin'


@dataclass(frozen=False, kw_only=True)
class BaseUserModel:
    uuid: UUID = field(default_factory=uuid4)
    tg_id: int
    username: str
    role: BaseUserRoles = field(default=BaseUserRoles.MEMBER)
    chats: set[uuid] = field(default_factory=set)


    def __eq__(self, other) -> bool:
        if isinstance(BaseUserModel, other):
            return self.uuid == other.uuid
        return NotImplemented
    
    def __hash__(self) -> int:
        return hash(self.uuid)
    
    def __str__(self) -> str:
        return f'uuid: {self.uuid}, tg_id: {self.tg_id}, username: {self.username}'

    def _validate_username(self):
        if (username := len(self.username)) < 3 or username > 15:
            raise UsernameException()