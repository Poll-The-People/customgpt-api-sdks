from enum import Enum


class UpdateSettingsResponse400DataMessage(str, Enum):
    LANGUAGE_PROFICIENCY_IS_REQUIRED = "Language Proficiency is required."
    PLEASE_UPLOAD_A_VALID_IMAGE_FILE_FOR_AVATAR = "Please upload a valid image file for avatar"
    PLEASE_UPLOAD_A_VALID_IMAGE_FILE_FOR_BACKGROUND = "Please upload a valid image file for background"

    def __str__(self) -> str:
        return str(self.value)
