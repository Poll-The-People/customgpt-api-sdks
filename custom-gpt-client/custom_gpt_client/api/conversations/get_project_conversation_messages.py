from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import CustomGPT, CustomGPTClient
from ...models.get_project_conversation_messages_order import GetProjectConversationMessagesOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: int,
    session_id: str,
    *,
    client: CustomGPT,
    page: Union[Unset, None, int] = 1,
    order: Union[Unset, None, GetProjectConversationMessagesOrder] = GetProjectConversationMessagesOrder.DESC,
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectId}/conversations/{sessionId}/messages".format(
        client.base_url, projectId=project_id, sessionId=session_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    json_order: Union[Unset, None, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value if order else None

    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(*, client: CustomGPTClient, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
        return None
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: CustomGPTClient, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: int,
    session_id: str,
    *,
    client: CustomGPT,
    page: Union[Unset, None, int] = 1,
    order: Union[Unset, None, GetProjectConversationMessagesOrder] = GetProjectConversationMessagesOrder.DESC,
) -> Response[Any]:
    """Retrieve messages that have been sent in a conversation.

     Get all the messages that have been sent in a conversation by `projectId` and `sessionId`.

    Args:
        project_id (int):  Example: 1.
        session_id (str):  Example: 1.
        page (Union[Unset, None, int]):  Default: 1.
        order (Union[Unset, None, GetProjectConversationMessagesOrder]):  Default:
            GetProjectConversationMessagesOrder.DESC. Example: desc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        session_id=session_id,
        client=client,
        page=page,
        order=order,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    project_id: int,
    session_id: str,
    *,
    client: CustomGPT,
    page: Union[Unset, None, int] = 1,
    order: Union[Unset, None, GetProjectConversationMessagesOrder] = GetProjectConversationMessagesOrder.DESC,
) -> Response[Any]:
    """Retrieve messages that have been sent in a conversation.

     Get all the messages that have been sent in a conversation by `projectId` and `sessionId`.

    Args:
        project_id (int):  Example: 1.
        session_id (str):  Example: 1.
        page (Union[Unset, None, int]):  Default: 1.
        order (Union[Unset, None, GetProjectConversationMessagesOrder]):  Default:
            GetProjectConversationMessagesOrder.DESC. Example: desc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        session_id=session_id,
        client=client,
        page=page,
        order=order,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
