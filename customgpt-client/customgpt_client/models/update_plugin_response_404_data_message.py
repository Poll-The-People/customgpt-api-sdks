from enum import Enum


class UpdatePluginResponse404DataMessage(str, Enum):
    PLUGIN_FOR_PROJECT_WITH_ID_PROJECTID_NOT_FOUND = "Plugin for project with id {projectId} not found"
    PROJECT_PLUGIN_ID_IS_REQUIRED = "Project plugin id is required"
    PROJECT_PLUGIN_WITH_ID_PLUGINID_NOT_FOUND = "Project plugin with id {pluginId} not found"

    def __str__(self) -> str:
        return str(self.value)
