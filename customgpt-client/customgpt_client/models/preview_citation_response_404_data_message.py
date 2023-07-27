from enum import Enum


class PreviewCitationResponse404DataMessage(str, Enum):
    PAGE_ID_IS_REQUIRED = "Page id is required"
    PAGE_WITH_ID_PAGEID_NOT_FOUND = "Page with id {pageId} not found"

    def __str__(self) -> str:
        return str(self.value)
