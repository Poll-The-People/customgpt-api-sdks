from enum import Enum


class ConversationsReportsFiltersItem(str, Enum):
    AVERAGE_QUERIES_PER_CONVERSATION = "average_queries_per_conversation"
    TOTAL = "total"

    def __str__(self) -> str:
        return str(self.value)
