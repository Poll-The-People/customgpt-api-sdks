from enum import Enum


class GetConversationsOrderBy(str, Enum):
    CREATED_AT = "created_at"
    ID = "id"

    def __str__(self) -> str:
        return str(self.value)
