from enum import Enum


class ProjectSourceSettingsDataRefreshFrequency(str, Enum):
    ADVANCED = "advanced"
    DAILY = "daily"
    MONTHLY = "monthly"
    NEVER = "never"
    WEEKLY = "weekly"

    def __str__(self) -> str:
        return str(self.value)
