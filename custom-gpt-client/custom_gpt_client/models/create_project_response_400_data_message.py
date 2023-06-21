from enum import Enum


class CreateProjectResponse400DataMessage(str, Enum):
    PROJECT_NAME_CANT_BE_EMPTY = "Project name can't be empty"
    SITEMAP_PATH_CANT_BE_EMPTY = "Sitemap path can't be empty"
    YOU_HAVE_REACHED_YOUR_MONTHLY_PROJECT_LIMIT = "You have reached your monthly project limit"

    def __str__(self) -> str:
        return str(self.value)
