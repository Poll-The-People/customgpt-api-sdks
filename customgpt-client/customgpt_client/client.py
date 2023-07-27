import ssl
from typing import Any, Dict, Union

import attr

from customgpt_client.api.citations import get_citation
from customgpt_client.api.conversations import (
    create_conversation,
    delete_conversation,
    get_conversations,
    messages_conversation,
    send_message,
    update_conversation,
)
from customgpt_client.api.pages import delete_page, get_pages, preview_citation, reindex_page
from customgpt_client.api.project_plugins import create_plugin, get_plugin, update_plugin
from customgpt_client.api.project_settings import get_settings, update_settings
from customgpt_client.api.projects import (
    create_project,
    delete_project,
    get_project,
    list_projects,
    stats_project,
    update_project,
)
from customgpt_client.api.sources import create_source, delete_source, list_sources
from customgpt_client.api.users import get_user, update_user
from customgpt_client.models import (
    CreateConversationJsonBody,
    CreatePluginJsonBody,
    CreateProjectMultipartData,
    CreateSourceMultipartData,
    SendMessageJsonBody,
    UpdateConversationJsonBody,
    UpdatePluginJsonBody,
    UpdateProjectMultipartData,
    UpdateSettingsMultipartData,
    UpdateUserMultipartData,
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

            return get_pages.sync_detailed(client=client, *args, **kwargs)

        def aget(*args: Any, **kwargs: Any):
            client = set_client()

            return get_pages.asyncio_detailed(client=client, *args, **kwargs)

        def delete(*args: Any, **kwargs: Any):
            client = set_client()

            return delete_page.sync_detailed(client=client, *args, **kwargs)

        def adelete(*args: Any, **kwargs: Any):
            client = set_client()

            return delete_page.asyncio_detailed(client=client, *args, **kwargs)

        def reindex(*args: Any, **kwargs: Any):
            client = set_client()

            return reindex_page.sync_detailed(client=client, *args, **kwargs)

        def areindex(*args: Any, **kwargs: Any):
            client = set_client()

            return reindex_page.asyncio_detailed(client=client, *args, **kwargs)

        def preview(*args: Any, **kwargs: Any):
            client = set_client()

            return preview_citation.sync_detailed(client=client, *args, **kwargs)

        def apreview(*args: Any, **kwargs: Any):
            client = set_client()

            return preview_citation.asyncio_detailed(client=client, *args, **kwargs)

    class ProjectSettings:
        def get(*args: Any, **kwargs: Any):
            client = set_client()

            return get_settings.sync_detailed(client=client, *args, **kwargs)

        def aget(*args: Any, **kwargs: Any):
            client = set_client()

            return get_settings.asyncio_detailed(client=client, *args, **kwargs)

        def update(*args: Any, **kwargs: Any):
            client = set_client()
            fields = [
                "chat_bot_avatar",
                "chat_bot_bg",
                "default_prompt",
                "example_questions",
                "response_source",
                "chatbot_msg_lang",
                "chatbot_color",
                "persona_instructions",
            ]
            json = pluck_data(fields, kwargs)
            kwargs["multipart_data"] = UpdateSettingsMultipartData(**json)

            return update_settings.sync_detailed(client=client, *args, **kwargs)

        def aupdate(*args: Any, **kwargs: Any):
            client = set_client()
            fields = [
                "chat_bot_avatar",
                "chat_bot_bg",
                "default_prompt",
                "example_questions",
                "response_source",
                "chatbot_msg_lang",
                "chatbot_color",
                "persona_instructions",
            ]
            json = pluck_data(fields, kwargs)
            kwargs["multipart_data"] = UpdateSettingsMultipartData(**json)

            return update_settings.asyncio_detailed(client=client, *args, **kwargs)

    class ProjectPlugins:
        def get(*args: Any, **kwargs: Any):
            client = set_client()

            return get_plugin.sync_detailed(client=client, *args, **kwargs)

        def aget(*args: Any, **kwargs: Any):
            client = set_client()

            return get_plugin.asyncio_detailed(client=client, *args, **kwargs)

        def update(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["model_name", "human_name", "keywords", "description", "is_active"]
            json = pluck_data(fields, kwargs)
            kwargs["json_body"] = UpdatePluginJsonBody(**json)

            return update_plugin.sync_detailed(client=client, *args, **kwargs)

        def aupdate(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["model_name", "human_name", "keywords", "description", "is_active"]
            json = pluck_data(fields, kwargs)
            kwargs["json_body"] = UpdatePluginJsonBody(**json)

            return update_plugin.asyncio_detailed(client=client, *args, **kwargs)

        def create(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["model_name", "human_name", "keywords", "description", "is_active"]
            json = pluck_data(fields, kwargs)
            kwargs["json_body"] = CreatePluginJsonBody(**json)

            return create_plugin.sync_detailed(client=client, *args, **kwargs)

        def acreate(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["model_name", "human_name", "keywords", "description", "is_active"]
            json = pluck_data(fields, kwargs)
            kwargs["json_body"] = CreatePluginJsonBody(**json)

            return create_plugin.asyncio_detailed(client=client, *args, **kwargs)

    class Conversation:
        def get(*args: Any, **kwargs: Any):
            client = set_client()

            return get_conversations.sync_detailed(client=client, *args, **kwargs)

        def aget(*args: Any, **kwargs: Any):
            client = set_client()

            return get_conversations.asyncio_detailed(client=client, *args, **kwargs)

        def create(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["name"]
            json = pluck_data(fields, kwargs)
            kwargs["json_body"] = CreateConversationJsonBody(**json)

            return create_conversation.sync_detailed(client=client, *args, **kwargs)

        def acreate(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["name"]
            json = pluck_data(fields, kwargs)
            kwargs["json_body"] = CreateConversationJsonBody(**json)

            return create_conversation.asyncio_detailed(client=client, *args, **kwargs)

        def update(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["name"]
            json = pluck_data(fields, kwargs)
            kwargs["json_body"] = UpdateConversationJsonBody(**json)

            return update_conversation.sync_detailed(client=client, *args, **kwargs)

        def aupdate(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["name"]
            json = pluck_data(fields, kwargs)
            kwargs["json_body"] = UpdateConversationJsonBody(**json)

            return update_conversation.asyncio_detailed(client=client, *args, **kwargs)

        def delete(*args: Any, **kwargs: Any):
            client = set_client()

            return delete_conversation.sync_detailed(client=client, *args, **kwargs)

        def adelete(*args: Any, **kwargs: Any):
            client = set_client()

            return delete_conversation.asyncio_detailed(client=client, *args, **kwargs)

        def messages(*args: Any, **kwargs: Any):
            client = set_client()

            return messages_conversation.sync_detailed(client=client, *args, **kwargs)

        def amessages(*args: Any, **kwargs: Any):
            client = set_client()

            return messages_conversation.asyncio_detailed(client=client, *args, **kwargs)

        def send(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["prompt"]
            json = pluck_data(fields, kwargs)
            kwargs["json_body"] = SendMessageJsonBody(**json)

            return send_message.sync_detailed(client=client, *args, **kwargs)

        def asend(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["prompt"]
            json = pluck_data(fields, kwargs)
            kwargs["json_body"] = SendMessageJsonBody(**json)

            return send_message.asyncio_detailed(client=client, *args, **kwargs)

    class Citation:
        def get(*args: Any, **kwargs: Any):
            client = set_client()

            return get_citation.sync_detailed(client=client, *args, **kwargs)

        def aget(*args: Any, **kwargs: Any):
            client = set_client()

            return get_citation.asyncio_detailed(client=client, *args, **kwargs)

    class Source:
        def list(*args: Any, **kwargs: Any):
            client = set_client()

            return list_sources.sync_detailed(client=client, *args, **kwargs)

        def alist(*args: Any, **kwargs: Any):
            client = set_client()

            return list_sources.asyncio_detailed(client=client, *args, **kwargs)

        def create(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["sitemap_path", "file_data_retension", "file"]
            json = pluck_data(fields, kwargs)
            kwargs["multipart_data"] = CreateSourceMultipartData(**json)

            return create_source.sync_detailed(client=client, *args, **kwargs)

        def acreate(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["sitemap_path", "file_data_retension", "file"]
            json = pluck_data(fields, kwargs)
            kwargs["multipart_data"] = CreateSourceMultipartData(**json)

            return create_source.asyncio_detailed(client=client, *args, **kwargs)

        def delete(*args: Any, **kwargs: Any):
            client = set_client()

            return delete_source.sync_detailed(client=client, *args, **kwargs)

        def adelete(*args: Any, **kwargs: Any):
            client = set_client()

            return delete_source.asyncio_detailed(client=client, *args, **kwargs)

    class User:
        def get(*args: Any, **kwargs: Any):
            client = set_client()

            return get_user.sync_detailed(client=client, *args, **kwargs)

        def aget(*args: Any, **kwargs: Any):
            client = set_client()

            return get_user.asyncio_detailed(client=client, *args, **kwargs)

        def update(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["profile_photo", "name"]
            json = pluck_data(fields, kwargs)
            kwargs["multipart_data"] = UpdateUserMultipartData(**json)

            return update_user.sync_detailed(client=client, *args, **kwargs)

        def aupdate(*args: Any, **kwargs: Any):
            client = set_client()
            fields = ["profile_photo", "name"]
            json = pluck_data(fields, kwargs)
            kwargs["multipart_data"] = UpdateUserMultipartData(**json)

            return update_user.asyncio_detailed(client=client, *args, **kwargs)
