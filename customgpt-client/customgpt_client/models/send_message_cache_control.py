from enum import Enum


class SendMessageCacheControl(str, Enum):
    NO_CACHE = "no-cache"

    def __str__(self) -> str:
        return str(self.value)
