from enum import Enum


class ProjectAnalyticsTrafficSourcesItemRequestSource(str, Enum):
    AI_ASSISTANT = "ai-assistant"
    API = "api"
    EMBED = "embed"
    INSTANT_VIEWER = "instant-viewer"
    LIVECHAT = "livechat"
    SGE = "sge"
    WEB = "web"

    def __str__(self) -> str:
        return str(self.value)
