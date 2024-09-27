from enum import Enum


class UpdateSourceResponse404DataMessage(str, Enum):
    PROJECT_SOURCE_ID_IS_REQUIRED = "Project source id is required"
    PROJECT_SOURCE_WITH_ID_SOURCEID_NOT_FOUND = "Project source with id {sourceId} not found"

    def __str__(self) -> str:
        return str(self.value)
