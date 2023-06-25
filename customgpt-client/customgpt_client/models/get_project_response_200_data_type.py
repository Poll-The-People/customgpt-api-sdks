from enum import Enum


class GetProjectResponse200DataType(str, Enum):
    SITEMAP = "SITEMAP"
    URL = "URL"

    def __str__(self) -> str:
        return str(self.value)
