from enum import Enum


class AnalysisReportsInterval(str, Enum):
    DAILY = "daily"
    WEEKLY = "weekly"

    def __str__(self) -> str:
        return str(self.value)
