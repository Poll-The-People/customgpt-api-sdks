from enum import Enum


class SynchronizeSourceResponse201DataSettingsRefreshExistingPages(str, Enum):
    ALWAYS = "always"
    IF_UPDATED = "if_updated"
    NEVER = "never"

    def __str__(self) -> str:
        return str(self.value)
