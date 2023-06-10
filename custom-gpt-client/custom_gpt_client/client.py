import ssl
from typing import Any, Dict, Union

import attr

from custom_gpt_client.api.citations import get_open_graph_data_for_citation
from custom_gpt_client.api.conversations import (
    create_project_conversation,
    delete_project_conversation,
    get_project_conversation_messages,
    get_project_conversations,
    send_message_to_conversation,
    update_project_conversation,
)
from custom_gpt_client.api.pages import delete_project_pages, get_project_pages
from custom_gpt_client.api.project_settings import get_project_settings, update_project_settings
from custom_gpt_client.api.projects import (
    create_project,
    delete_project,
    get_project,
    get_project_stats,
    list_projects,
    update_project,
)
from custom_gpt_client.api.users import get_user_profile, update_user_profile


@attr.s(auto_attribs=True)
class CustomGPTClient:
    """A class for keeping track of data related to the API

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

    base_url: str
    cookies: Dict[str, str] = attr.ib(factory=dict, kw_only=True)
    headers: Dict[str, str] = attr.ib(factory=dict, kw_only=True)
    timeout: float = attr.ib(5.0, kw_only=True)
    verify_ssl: Union[str, bool, ssl.SSLContext] = attr.ib(True, kw_only=True)
    raise_on_unexpected_status: bool = attr.ib(False, kw_only=True)
    follow_redirects: bool = attr.ib(False, kw_only=True)

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in all endpoints"""
        return {**self.headers}

    def with_headers(self, headers: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional headers"""
        return attr.evolve(self, headers={**self.headers, **headers})

    def get_cookies(self) -> Dict[str, str]:
        return {**self.cookies}

    def with_cookies(self, cookies: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional cookies"""
        return attr.evolve(self, cookies={**self.cookies, **cookies})

    def get_timeout(self) -> float:
        return self.timeout

    def with_timeout(self, timeout: float) -> "Client":
        """Get a new client matching this one with a new timeout (in seconds)"""
        return attr.evolve(self, timeout=timeout)


@attr.s(auto_attribs=True)
class CustomGPT(CustomGPTClient):
    """A Client which has been authenticated for use on secured endpoints"""

    token: str
    prefix: str = "Bearer"
    auth_header_name: str = "Authorization"

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in authenticated endpoints"""
        auth_header_value = f"{self.prefix} {self.token}" if self.prefix else self.token
        return {self.auth_header_name: auth_header_value, **self.headers}

    def list_projects(self, *args: Any, **kwargs: Any):
        return list_projects.sync_detailed(client=self, *args, **kwargs)

    def create_project(self, *args: Any, **kwargs: Any):
        return create_project.sync_detailed(client=self, *args, **kwargs)

    def get_project(self, *args: Any, **kwargs: Any):
        return get_project.sync_detailed(client=self, *args, **kwargs)

    def update_project(self, *args: Any, **kwargs: Any):
        return update_project.sync_detailed(client=self, *args, **kwargs)

    def delete_project(self, *args: Any, **kwargs: Any):
        return delete_project.sync_detailed(client=self, *args, **kwargs)

    def get_project_stats(self, *args: Any, **kwargs: Any):
        return get_project_stats.sync_detailed(client=self, *args, **kwargs)

    def get_project_pages(self, *args: Any, **kwargs: Any):
        return get_project_pages.sync_detailed(client=self, *args, **kwargs)

    def delete_project_pages(self, *args: Any, **kwargs: Any):
        return delete_project_pages.sync_detailed(client=self, *args, **kwargs)

    def get_project_settings(self, *args: Any, **kwargs: Any):
        return get_project_settings.sync_detailed(client=self, *args, **kwargs)

    def update_project_settings(self, *args: Any, **kwargs: Any):
        return update_project_settings.sync_detailed(client=self, *args, **kwargs)

    def get_project_conversations(self, *args: Any, **kwargs: Any):
        return get_project_conversations.sync_detailed(client=self, *args, **kwargs)

    def create_project_conversation(self, *args: Any, **kwargs: Any):
        return create_project_conversation.sync_detailed(client=self, *args, **kwargs)

    def update_project_conversation(self, *args: Any, **kwargs: Any):
        return update_project_conversation.sync_detailed(client=self, *args, **kwargs)

    def delete_project_conversation(self, *args: Any, **kwargs: Any):
        return delete_project_conversation.sync_detailed(client=self, *args, **kwargs)

    def get_project_conversation_messages(self, *args: Any, **kwargs: Any):
        return get_project_conversation_messages.sync_detailed(client=self, *args, **kwargs)

    def send_message_to_conversation(self, *args: Any, **kwargs: Any):
        return send_message_to_conversation.sync_detailed(client=self, *args, **kwargs)

    def get_open_graph_data_for_citation(self, *args: Any, **kwargs: Any):
        return get_open_graph_data_for_citation.sync_detailed(client=self, *args, **kwargs)

    def get_user_profile(self, *args: Any, **kwargs: Any):
        return get_user_profile.sync_detailed(client=self, *args, **kwargs)

    def update_user_profile(self, *args: Any, **kwargs: Any):
        return update_user_profile.sync_detailed(client=self, *args, **kwargs)