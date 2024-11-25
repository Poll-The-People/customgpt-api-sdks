from enum import Enum


class GetProjectSettingsResponse200DataCitationsViewType(str, Enum):
    HIDE = "hide"
    SHOW = "show"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
