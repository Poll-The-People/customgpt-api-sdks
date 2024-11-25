from enum import Enum


class SynchronizeSourceResponse403DataMessage(str, Enum):
    NEXT_INSTANT_SYNC_WILL_BE_AVAILABLE_IN_SECONDS_SECONDS = (
        "Next instant sync will be available in \{seconds\} seconds"
    )
    PROJECT_SOURCE_CANT_BE_SYNCED = "Project source can't be synced"
    YOUR_PLAN_NOT_ELIGIBLE_FOR_INSTANT_SYNC = "Your plan not eligible for instant sync"

    def __str__(self) -> str:
        return str(self.value)
