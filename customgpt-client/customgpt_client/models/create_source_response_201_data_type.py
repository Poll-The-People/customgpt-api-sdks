from enum import Enum


class CreateSourceResponse201DataType(str, Enum):
    SITEMAP = "sitemap"
    UPLOAD = "upload"

    def __str__(self) -> str:
        return str(self.value)
