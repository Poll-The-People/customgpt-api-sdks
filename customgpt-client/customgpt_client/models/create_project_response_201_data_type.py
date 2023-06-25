from enum import Enum


class CreateProjectResponse201DataType(str, Enum):
    SITEMAP = "SITEMAP"
    URL = "URL"

    def __str__(self) -> str:
        return str(self.value)
