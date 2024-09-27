from enum import Enum


class TrafficReportsResponse500Status(str, Enum):
    ERROR = "error"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
