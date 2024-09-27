from enum import Enum


class SynchronizeSourceResponse404Status(str, Enum):
    ERROR = "error"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
