from enum import Enum


class GetConversationsUserFilter(str, Enum):
    ALL = "all"
    ANONYMOUS = "anonymous"
    TEAM_MEMBER = "team_member"

    def __str__(self) -> str:
        return str(self.value)
