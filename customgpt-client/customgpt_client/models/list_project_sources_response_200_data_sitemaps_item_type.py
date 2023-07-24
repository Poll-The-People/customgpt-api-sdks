from enum import Enum


class ListProjectSourcesResponse200DataSitemapsItemType(str, Enum):
    CRAWLER = "crawler"
    S3 = "S3"
    SITEMAP = "sitemap"
    UPLOAD = "upload"
    ZAPIER = "zapier"

    def __str__(self) -> str:
        return str(self.value)