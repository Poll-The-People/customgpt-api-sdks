from enum import Enum


class SendMessageJsonBodyResponseSource(str, Enum):
    DEFAULT = "default"
    OPENAI_CONTENT = "openai_content"
    OWN_CONTENT = "own_content"

    def __str__(self) -> str:
        return str(self.value)
