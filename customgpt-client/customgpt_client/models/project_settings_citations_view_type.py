from enum import Enum


class ProjectSettingsCitationsViewType(str, Enum):
    HIDE = "hide"
    SHOW = "show"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
