from enum import Enum


class ListSourcesResponse200DataSitemapsItemType(str, Enum):
    SITEMAP = "sitemap"
    UPLOAD = "upload"

    def __str__(self) -> str:
        return str(self.value)
