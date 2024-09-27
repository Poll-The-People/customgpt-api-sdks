from enum import Enum


class ListSourcesResponse200DataUploadsSettingsDataRefreshFrequency(str, Enum):
    ADVANCED = "advanced"
    DAILY = "daily"
    MONTHLY = "monthly"
    NEVER = "never"
    WEEKLY = "weekly"

    def __str__(self) -> str:
        return str(self.value)
