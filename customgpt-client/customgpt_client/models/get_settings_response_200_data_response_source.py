from enum import Enum


class GetSettingsResponse200DataResponseSource(str, Enum):
    DEFAULT = "Default"
    MY_CONTENT = "My Content"
    MY_CONTENT_CHATGPT = "My Content + ChatGPT"

    def __str__(self) -> str:
        return str(self.value)
