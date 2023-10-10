from enum import Enum


class UpdateSettingsMultipartDataCitationsViewType(str, Enum):
    HIDE = "hide"
    SHOW = "show"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
