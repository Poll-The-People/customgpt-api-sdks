from enum import Enum


class ListSourcesResponse200DataSitemapsItemPagesItemCrawlStatus(str, Enum):
    FAILED = "failed"
    LIMITED = "limited"
    NA = "n/a"
    OK = "ok"
    QUEUED = "queued"

    def __str__(self) -> str:
        return str(self.value)
