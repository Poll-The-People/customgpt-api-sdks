from enum import Enum


class UpdateMetadataResponse200Status(str, Enum):
    ERROR = "error"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
