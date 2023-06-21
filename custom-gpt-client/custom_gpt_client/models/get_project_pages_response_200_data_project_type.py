from enum import Enum


class GetProjectPagesResponse200DataProjectType(str, Enum):
    SITEMAP = "SITEMAP"
    URL = "URL"

    def __str__(self) -> str:
        return str(self.value)
