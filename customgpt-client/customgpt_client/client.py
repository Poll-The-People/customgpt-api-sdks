import ssl
from typing import Any, Dict, Union

import attr

from customgpt_client.api.citations import get_open_graph_data_for_citation
from customgpt_client.api.conversations import (
    create_project_conversation,
    delete_project_conversation,
    get_project_conversations,
    messages,
    send_message_to_conversation,
    update_project_conversation,
)
from customgpt_client.api.pages import delete_project_page, get_project_pages, preview
from customgpt_client.api.project_plugins import create_project_plugin, get_project_plugins, update_project_plugin
from customgpt_client.api.project_settings import get_project_settings, update_project_settings
from customgpt_client.api.projects import (
    create_project,
    delete_project,
    get_project,
    list_projects,
    stats_project,
    update_project,
)
from customgpt_client.api.sources import create_project_source, delete_project_source, list_project_sources
from customgpt_client.api.users import get_user_profile, update_user_profile
from customgpt_client.models import (
    CreateProjectConversationJsonBody,
    CreateProjectMultipartData,
    CreateProjectPluginJsonBody,
    CreateProjectSourceMultipartData,
    SendMessageToConversationJsonBody,
    UpdateProjectConversationJsonBody,
    UpdateProjectMultipartData,
    UpdateProjectPluginJsonBody,
    UpdateProjectSettingsMultipartData,
    UpdateUserProfileMultipartData,
)


def set_client():
    api_key = CustomGPT.api_key
    base_url = CustomGPT.base_url if hasattr(CustomGPT, "base_url") else "https://app.customgpt.ai"
    timeout = CustomGPT.timeout if hasattr(CustomGPT, "timeout") else 100.0
    return CustomGPT(api_key=api_key, base_url=base_url, timeout=timeout)


def pluck_data(fields, kwargs):
    json = {}
    for field in fields:
        if field in kwargs:
            json[field] = kwargs.pop(field)
    return json


@attr.s(auto_attribs=True)
class CustomGPT:
    """A Client which has been authenticated for use on secured endpoints
    Attributes:
        base_url: The base URL for the API, all requests are made to a relative path to this URL
        cookies: A dictionary of cookies to be sent with every request
        headers: A dictionary of headers to be sent with every request
        timeout: The maximum amount of a time in seconds a request can take. API functions will raise
            httpx.TimeoutException if this is exceeded.
        verify_ssl: Whether or not to verify the SSL certificate of the API server. This should be True in production,
            but can be set to False for testing purposes.
        raise_on_unexpected_status: Whether or not to raise an errors.UnexpectedStatus if the API returns a
            status code that was not documented in the source OpenAPI document.
        follow_redirects: Whether or not to follow redirects. Default value is False.
    """

    api_key: str
    prefix: str = "Bearer"
    auth_header_name: str = "Authorization"
    base_url: str = attr.ib("https://app.customgpt.ai")
    cookies: Dict[str, str] = attr.ib(factory=dict, kw_only=True)
    headers: Dict[str, str] = attr.ib(factory=dict, kw_only=True)
    timeout: float = attr.ib(5.0, kw_only=True)
    verify_ssl: Union[str, bool, ssl.SSLContext] = attr.ib(True, kw_only=True)
    raise_on_unexpected_status: bool = attr.ib(False, kw_only=True)
    follow_redirects: bool = attr.ib(False, kw_only=True)

    def with_headers(self, headers: Dict[str, str]) -> "CustomGPT":
        """Get a new client matching this one with additional headers"""
        return attr.evolve(self, headers={**self.headers, **headers})

    def get_cookies(self) -> Dict[str, str]:
        return {**self.cookies}

    def with_cookies(self, cookies: Dict[str, str]) -> "CustomGPT":
        """Get a new client matching this one with additional cookies"""
        return attr.evolve(self, cookies={**self.cookies, **cookies})

    def get_timeout(self) -> float:
        return self.timeout

    def with_timeout(self, timeout: float) -> "CustomGPT":
        """Get a new client matching this one with a new timeout (in seconds)"""
        return attr.evolve(self, timeout=timeout)

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in authenticated endpoints"""
        auth_header_value = f"{self.prefix} {self.api_key}" if self.prefix else self.api_key
        return {self.auth_header_name: auth_header_value, **self.headers}

    class Project:
        def list(*args: Any, **kwargs: Any):
            client = set_client()

            return list_projects.sync_detailed(client=client, *args, **kwargs)

        def alist(*args: Any, **kwargs: Any):
            client = set_client()

            return list_projects.asyncio_detailed(client=client, *args, **kwargs)

        def create(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["project_name", "sitemap_path", "file_data_retension", "file"]
            json = pluck_data(fields, kwargs)
            kwargs["multipart_data"] = CreateProjectMultipartData(**json)

            return create_project.sync_detailed(client=client, *args, **kwargs)

        def acreate(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["project_name", "sitemap_path", "file_data_retension", "file"]
            json = pluck_data(fields, kwargs)
            kwargs["multipart_data"] = CreateProjectMultipartData(**json)

            return create_project.asyncio_detailed(client=client, *args, **kwargs)

        def get(*args: Any, **kwargs: Any):
            client = set_client()

            return get_project.sync_detailed(client=client, *args, **kwargs)

        def aget(*args: Any, **kwargs: Any):
            client = set_client()

            return get_project.asyncio_detailed(client=client, *args, **kwargs)

        def update(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["project_name", "is_shared", "sitemap_path", "file_data_retension", "file"]
            json = pluck_data(fields, kwargs)
            kwargs["multipart_data"] = UpdateProjectMultipartData(**json)

            return update_project.sync_detailed(client=client, *args, **kwargs)

        def aupdate(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["project_name", "is_shared", "sitemap_path", "file_data_retension", "file"]
            json = pluck_data(fields, kwargs)
            kwargs["multipart_data"] = UpdateProjectMultipartData(**json)

            return update_project.asyncio_detailed(client=client, *args, **kwargs)

        def delete(*args: Any, **kwargs: Any):
            client = set_client()

            return delete_project.sync_detailed(client=client, *args, **kwargs)

        def adelete(*args: Any, **kwargs: Any):
            client = set_client()

            return delete_project.asyncio_detailed(client=client, *args, **kwargs)

        def stats(*args: Any, **kwargs: Any):
            client = set_client()

            return stats_project.sync_detailed(client=client, *args, **kwargs)

        def astats(*args: Any, **kwargs: Any):
            client = set_client()

            return stats_project.asyncio_detailed(client=client, *args, **kwargs)

    class Page:
        def get(*args: Any, **kwargs: Any):
            client = set_client()

            return get_project_pages.sync_detailed(client=client, *args, **kwargs)

        def aget(*args: Any, **kwargs: Any):
            client = set_client()

            return get_project_pages.asyncio_detailed(client=client, *args, **kwargs)

        def delete(*args: Any, **kwargs: Any):
            client = set_client()

            return delete_project_page.sync_detailed(client=client, *args, **kwargs)

        def adelete(*args: Any, **kwargs: Any):
            client = set_client()

            return delete_project_page.asyncio_detailed(client=client, *args, **kwargs)

        def preview(*args: Any, **kwargs: Any):
            client = set_client()

            return preview.sync_detailed(client=client, *args, **kwargs)

        def apreview(*args: Any, **kwargs: Any):
            client = set_client()

            return preview.asyncio_detailed(client=client, *args, **kwargs)

    class ProjectSettings:
        def get(*args: Any, **kwargs: Any):
            client = set_client()

            return get_project_settings.sync_detailed(client=client, *args, **kwargs)

        def aget(*args: Any, **kwargs: Any):
            client = set_client()

            return get_project_settings.asyncio_detailed(client=client, *args, **kwargs)

        def update(*args: Any, **kwargs: Any):
            client = set_client()
            fields = [
                "chat_bot_avatar",
                "chat_bot_bg",
                "default_prompt",
                "example_questions",
                "response_source",
                "chatbot_msg_lang",
            ]
            json = pluck_data(fields, kwargs)
            kwargs["multipart_data"] = UpdateProjectSettingsMultipartData(**json)

            return update_project_settings.sync_detailed(client=client, *args, **kwargs)

        def aupdate(*args: Any, **kwargs: Any):
            client = set_client()
            fields = [
                "chat_bot_avatar",
                "chat_bot_bg",
                "default_prompt",
                "example_questions",
                "response_source",
                "chatbot_msg_lang",
            ]
            json = pluck_data(fields, kwargs)
            kwargs["multipart_data"] = UpdateProjectSettingsMultipartData(**json)

            return update_project_settings.asyncio_detailed(client=client, *args, **kwargs)

    class ProjectPlugins:
        def get(*args: Any, **kwargs: Any):
            client = set_client()

            return get_project_plugins.sync_detailed(client=client, *args, **kwargs)

        def aget(*args: Any, **kwargs: Any):
            client = set_client()

            return get_project_plugins.asyncio_detailed(client=client, *args, **kwargs)

        def update(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["model_name", "human_name", "keywords", "description", "is_active"]
            json = pluck_data(fields, kwargs)
            kwargs["json_body"] = UpdateProjectPluginJsonBody(**json)

            return update_project_plugin.sync_detailed(client=client, *args, **kwargs)

        def aupdate(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["model_name", "human_name", "keywords", "description", "is_active"]
            json = pluck_data(fields, kwargs)
            kwargs["json_body"] = UpdateProjectPluginJsonBody(**json)

            return update_project_plugin.asyncio_detailed(client=client, *args, **kwargs)

        def create(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["model_name", "human_name", "keywords", "description", "is_active"]
            json = pluck_data(fields, kwargs)
            kwargs["json_body"] = CreateProjectPluginJsonBody(**json)

            return create_project_plugin.sync_detailed(client=client, *args, **kwargs)

        def acreate(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["model_name", "human_name", "keywords", "description", "is_active"]
            json = pluck_data(fields, kwargs)
            kwargs["json_body"] = CreateProjectPluginJsonBody(**json)

            return create_project_plugin.asyncio_detailed(client=client, *args, **kwargs)

    class Conversation:
        def get(*args: Any, **kwargs: Any):
            client = set_client()

            return get_project_conversations.sync_detailed(client=client, *args, **kwargs)

        def aget(*args: Any, **kwargs: Any):
            client = set_client()

            return get_project_conversations.asyncio_detailed(client=client, *args, **kwargs)

        def create(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["name"]
            json = pluck_data(fields, kwargs)
            kwargs["json_body"] = CreateProjectConversationJsonBody(**json)

            return create_project_conversation.sync_detailed(client=client, *args, **kwargs)

        def acreate(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["name"]
            json = pluck_data(fields, kwargs)
            kwargs["json_body"] = CreateProjectConversationJsonBody(**json)

            return create_project_conversation.asyncio_detailed(client=client, *args, **kwargs)

        def update(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["name"]
            json = pluck_data(fields, kwargs)
            kwargs["json_body"] = UpdateProjectConversationJsonBody(**json)

            return update_project_conversation.sync_detailed(client=client, *args, **kwargs)

        def aupdate(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["name"]
            json = pluck_data(fields, kwargs)
            kwargs["json_body"] = UpdateProjectConversationJsonBody(**json)

            return update_project_conversation.asyncio_detailed(client=client, *args, **kwargs)

        def delete(*args: Any, **kwargs: Any):
            client = set_client()

            return delete_project_conversation.sync_detailed(client=client, *args, **kwargs)

        def adelete(*args: Any, **kwargs: Any):
            client = set_client()

            return delete_project_conversation.asyncio_detailed(client=client, *args, **kwargs)

        def messages(*args: Any, **kwargs: Any):
            client = set_client()

            return messages.sync_detailed(client=client, *args, **kwargs)

        def amessages(*args: Any, **kwargs: Any):
            client = set_client()

            return messages.asyncio_detailed(client=client, *args, **kwargs)

        def send(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["prompt"]
            json = pluck_data(fields, kwargs)
            kwargs["json_body"] = SendMessageToConversationJsonBody(**json)

            return send_message_to_conversation.sync_detailed(client=client, *args, **kwargs)

        def asend(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["prompt"]
            json = pluck_data(fields, kwargs)
            kwargs["json_body"] = SendMessageToConversationJsonBody(**json)

            return send_message_to_conversation.asyncio_detailed(client=client, *args, **kwargs)

    class Citation:
        def get(*args: Any, **kwargs: Any):
            client = set_client()

            return get_open_graph_data_for_citation.sync_detailed(client=client, *args, **kwargs)

        def aget(*args: Any, **kwargs: Any):
            client = set_client()

            return get_open_graph_data_for_citation.asyncio_detailed(client=client, *args, **kwargs)

    class Source:
        def list(*args: Any, **kwargs: Any):
            client = set_client()

            return list_project_sources.sync_detailed(client=client, *args, **kwargs)

        def alist(*args: Any, **kwargs: Any):
            client = set_client()

            return list_project_sources.asyncio_detailed(client=client, *args, **kwargs)

        def create(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["sitemap_path", "file_data_retension", "file"]
            json = pluck_data(fields, kwargs)
            kwargs["multipart_data"] = CreateProjectSourceMultipartData(**json)

            return create_project_source.sync_detailed(client=client, *args, **kwargs)

        def acreate(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["sitemap_path", "file_data_retension", "file"]
            json = pluck_data(fields, kwargs)
            kwargs["multipart_data"] = CreateProjectSourceMultipartData(**json)

            return create_project_source.asyncio_detailed(client=client, *args, **kwargs)

        def delete(*args: Any, **kwargs: Any):
            client = set_client()

            return delete_project_source.sync_detailed(client=client, *args, **kwargs)

        def adelete(*args: Any, **kwargs: Any):
            client = set_client()

            return delete_project_source.asyncio_detailed(client=client, *args, **kwargs)

    class User:
        def get(*args: Any, **kwargs: Any):
            client = set_client()

            return get_user_profile.sync_detailed(client=client, *args, **kwargs)

        def aget(*args: Any, **kwargs: Any):
            client = set_client()

            return get_user_profile.asyncio_detailed(client=client, *args, **kwargs)

        def update(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["profile_photo", "name"]
            json = pluck_data(fields, kwargs)
            kwargs["multipart_data"] = UpdateUserProfileMultipartData(**json)

            return update_user_profile.sync_detailed(client=client, *args, **kwargs)

        def aupdate(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["profile_photo", "name"]
            json = pluck_data(fields, kwargs)
            kwargs["multipart_data"] = UpdateUserProfileMultipartData(**json)

            return update_user_profile.asyncio_detailed(client=client, *args, **kwargs)
