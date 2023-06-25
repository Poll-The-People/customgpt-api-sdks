from enum import Enum


class ListProjectsResponse200DataDataItemType(str, Enum):
    SITEMAP = "SITEMAP"
    URL = "URL"

    def __str__(self) -> str:
        return str(self.value)
