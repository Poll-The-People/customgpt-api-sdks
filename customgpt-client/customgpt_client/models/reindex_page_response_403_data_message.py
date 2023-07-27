from enum import Enum


class ReindexPageResponse403DataMessage(str, Enum):
    PAGE_WITH_ID_PAGEID_CANNOT_BE_REINDEXED = "Page with id {pageId} cannot be reindexed"

    def __str__(self) -> str:
        return str(self.value)
