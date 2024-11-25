from enum import Enum


class AnalysisReportsFiltersItem(str, Enum):
    CONVERSATIONS = "conversations"
    QUERIES = "queries"
    QUERIES_PER_CONVERSATION = "queries_per_conversation"

    def __str__(self) -> str:
        return str(self.value)
