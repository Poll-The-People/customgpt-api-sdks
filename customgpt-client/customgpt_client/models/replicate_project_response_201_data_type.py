from enum import Enum


class ReplicateProjectResponse201DataType(str, Enum):
    SITEMAP = "SITEMAP"
    URL = "URL"

    def __str__(self) -> str:
        return str(self.value)
