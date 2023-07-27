from enum import Enum


class ProjectSourceType(str, Enum):
    SITEMAP = "sitemap"
    UPLOAD = "upload"

    def __str__(self) -> str:
        return str(self.value)
