from enum import Enum


class CreateSourceResponse400DataMessage(str, Enum):
    OUR_SYSTEM_COULD_NOT_DETECT_ANY_PAGES_IN_YOUR_SITEMAP = "Our system could not detect any pages in your sitemap"
    OUR_SYSTEM_COULD_NOT_VALIDATE_YOUR_SITEMAP = "Our system could not validate your sitemap"
    SITEMAP_URL_IS_EMPTY = "Sitemap URL is empty"

    def __str__(self) -> str:
        return str(self.value)
