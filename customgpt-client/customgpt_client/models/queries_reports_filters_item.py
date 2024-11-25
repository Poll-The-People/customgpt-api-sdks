from enum import Enum


class QueriesReportsFiltersItem(str, Enum):
    QUERY_STATUS = "query_status"
    TOTAL = "total"

    def __str__(self) -> str:
        return str(self.value)
