from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...models.messages_order import MessagesOrder
from ...models.messages_response_200 import MessagesResponse200
from ...models.messages_response_401 import MessagesResponse401
from ...models.messages_response_404 import MessagesResponse404
from ...models.messages_response_500 import MessagesResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: int,
    session_id: str,
    *,
    client: {},
    page: Union[Unset, None, int] = 1,
    order: Union[Unset, None, MessagesOrder] = MessagesOrder.DESC,
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


def _parse_response(
    *, client: {}, response: httpx.Response
) -> Optional[Union[MessagesResponse200, MessagesResponse401, MessagesResponse404, MessagesResponse500]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = MessagesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = MessagesResponse401.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = MessagesResponse404.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = MessagesResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: {}, response: httpx.Response, content: Optional[bytes] = None
) -> Response[Union[MessagesResponse200, MessagesResponse401, MessagesResponse404, MessagesResponse500]]:
    parse = _parse_response(client=client, response=response)
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content if content is None else content,
        headers=response.headers,
        parsed=parse,
    )


def sync_detailed(
    project_id: int,
    session_id: str,
    *,
    client: {},
    page: Union[Unset, None, int] = 1,
    order: Union[Unset, None, MessagesOrder] = MessagesOrder.DESC,
):
    """Retrieve messages that have been sent in a conversation.

     Get all the messages that have been sent in a conversation by `projectId` and `sessionId`.

    Args:
        project_id (int):  Example: 1.
        session_id (str):  Example: 1.
        page (Union[Unset, None, int]):  Default: 1.
        order (Union[Unset, None, MessagesOrder]):  Default: MessagesOrder.DESC. Example: desc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[MessagesResponse200, MessagesResponse401, MessagesResponse404, MessagesResponse500]]
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


def sync(
    project_id: int,
    session_id: str,
    *,
    client: {},
    page: Union[Unset, None, int] = 1,
    order: Union[Unset, None, MessagesOrder] = MessagesOrder.DESC,
) -> Optional[Union[MessagesResponse200, MessagesResponse401, MessagesResponse404, MessagesResponse500]]:
    """Retrieve messages that have been sent in a conversation.

     Get all the messages that have been sent in a conversation by `projectId` and `sessionId`.

    Args:
        project_id (int):  Example: 1.
        session_id (str):  Example: 1.
        page (Union[Unset, None, int]):  Default: 1.
        order (Union[Unset, None, MessagesOrder]):  Default: MessagesOrder.DESC. Example: desc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[MessagesResponse200, MessagesResponse401, MessagesResponse404, MessagesResponse500]
    """

    return sync_detailed(
        project_id=project_id,
        session_id=session_id,
        client=client,
        page=page,
        order=order,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    session_id: str,
    *,
    client: {},
    page: Union[Unset, None, int] = 1,
    order: Union[Unset, None, MessagesOrder] = MessagesOrder.DESC,
) -> Response[Union[MessagesResponse200, MessagesResponse401, MessagesResponse404, MessagesResponse500]]:
    """Retrieve messages that have been sent in a conversation.

     Get all the messages that have been sent in a conversation by `projectId` and `sessionId`.

    Args:
        project_id (int):  Example: 1.
        session_id (str):  Example: 1.
        page (Union[Unset, None, int]):  Default: 1.
        order (Union[Unset, None, MessagesOrder]):  Default: MessagesOrder.DESC. Example: desc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[MessagesResponse200, MessagesResponse401, MessagesResponse404, MessagesResponse500]]
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


async def asyncio(
    project_id: int,
    session_id: str,
    *,
    client: {},
    page: Union[Unset, None, int] = 1,
    order: Union[Unset, None, MessagesOrder] = MessagesOrder.DESC,
) -> Optional[Union[MessagesResponse200, MessagesResponse401, MessagesResponse404, MessagesResponse500]]:
    """Retrieve messages that have been sent in a conversation.

     Get all the messages that have been sent in a conversation by `projectId` and `sessionId`.

    Args:
        project_id (int):  Example: 1.
        session_id (str):  Example: 1.
        page (Union[Unset, None, int]):  Default: 1.
        order (Union[Unset, None, MessagesOrder]):  Default: MessagesOrder.DESC. Example: desc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[MessagesResponse200, MessagesResponse401, MessagesResponse404, MessagesResponse500]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            session_id=session_id,
            client=client,
            page=page,
            order=order,
        )
    ).parsed
