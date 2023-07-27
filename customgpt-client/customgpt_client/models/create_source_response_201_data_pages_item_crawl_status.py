from enum import Enum


class CreateSourceResponse201DataPagesItemCrawlStatus(str, Enum):
    FAILED = "failed"
    LIMITED = "limited"
    NA = "n/a"
    OK = "ok"
    QUEUED = "queued"

    def __str__(self) -> str:
        return str(self.value)
