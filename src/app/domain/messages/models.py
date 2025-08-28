from dataclasses import dataclass, field
from uuid import uuid4, UUID


@dataclass(frozen=True)
class Text:
    value: str

    def __post_init__(self):
        self._validate(self)

    def _validate(self) -> True:
        """Какая-то валидация по длине или символам ;3"""
        ...


@dataclass(frozen=True, kw_only=True)
class BaseMessage:
    uuid: UUID = field(default_factory=uuid4)
    text: Text
    sender_id: UUID
    created_at: datetime = field(default_factory=datetime.utcnow)

    def __eq__(self, other):
        if isinstance(BaseMessage, other):
            return self.uuid == other.uuid
        return NotImplemented

    def __hash__(self):
        return hash(self.uuid)
