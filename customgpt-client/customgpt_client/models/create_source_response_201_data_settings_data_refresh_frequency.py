from enum import Enum


class CreateSourceResponse201DataSettingsDataRefreshFrequency(str, Enum):
    ADVANCED = "advanced"
    DAILY = "daily"
    MONTHLY = "monthly"
    NEVER = "never"
    WEEKLY = "weekly"

    def __str__(self) -> str:
        return str(self.value)
