from enum import Enum


class TrafficReportsFiltersItem(str, Enum):
    SOURCES = "sources"

    def __str__(self) -> str:
        return str(self.value)
