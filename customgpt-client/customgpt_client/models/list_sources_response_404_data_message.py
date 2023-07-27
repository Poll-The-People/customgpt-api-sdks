from enum import Enum


class ListSourcesResponse404DataMessage(str, Enum):
    PROJECT_ID_IS_REQUIRED = "Project id is required"
    PROJECT_WITH_ID_PROJECTID_NOT_FOUND = "Project with id {projectId} not found"

    def __str__(self) -> str:
        return str(self.value)
