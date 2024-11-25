from enum import Enum


class SynchronizeSourceResponse201DataType(str, Enum):
    SITEMAP = "sitemap"
    UPLOAD = "upload"

    def __str__(self) -> str:
        return str(self.value)
