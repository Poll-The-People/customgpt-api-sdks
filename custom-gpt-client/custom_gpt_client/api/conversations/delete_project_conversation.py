from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...models.delete_project_conversation_response_200 import DeleteProjectConversationResponse200
from ...models.delete_project_conversation_response_401 import DeleteProjectConversationResponse401
from ...models.delete_project_conversation_response_404 import DeleteProjectConversationResponse404
from ...models.delete_project_conversation_response_500 import DeleteProjectConversationResponse500
from ...types import Response


def _get_kwargs(
    project_id: int,
    session_id: str,
    *,
    client: {},
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectId}/conversations/{sessionId}".format(
        client.base_url, projectId=project_id, sessionId=session_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(
    *, client: {}, response: httpx.Response
) -> Optional[
    Union[
        DeleteProjectConversationResponse200,
        DeleteProjectConversationResponse401,
        DeleteProjectConversationResponse404,
        DeleteProjectConversationResponse500,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DeleteProjectConversationResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = DeleteProjectConversationResponse401.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = DeleteProjectConversationResponse404.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = DeleteProjectConversationResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: {}, response: httpx.Response, content: Optional[bytes] = None
) -> Response[
    Union[
        DeleteProjectConversationResponse200,
        DeleteProjectConversationResponse401,
        DeleteProjectConversationResponse404,
        DeleteProjectConversationResponse500,
    ]
]:
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
):
    """Delete a conversation.

     Delete a conversation by `projectId` and `sessionId`.

    Args:
        project_id (int):
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteProjectConversationResponse200, DeleteProjectConversationResponse401, DeleteProjectConversationResponse404, DeleteProjectConversationResponse500]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        session_id=session_id,
        client=client,
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
) -> Optional[
    Union[
        DeleteProjectConversationResponse200,
        DeleteProjectConversationResponse401,
        DeleteProjectConversationResponse404,
        DeleteProjectConversationResponse500,
    ]
]:
    """Delete a conversation.

     Delete a conversation by `projectId` and `sessionId`.

    Args:
        project_id (int):
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteProjectConversationResponse200, DeleteProjectConversationResponse401, DeleteProjectConversationResponse404, DeleteProjectConversationResponse500]
    """

    return sync_detailed(
        project_id=project_id,
        session_id=session_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    session_id: str,
    *,
    client: {},
) -> Response[
    Union[
        DeleteProjectConversationResponse200,
        DeleteProjectConversationResponse401,
        DeleteProjectConversationResponse404,
        DeleteProjectConversationResponse500,
    ]
]:
    """Delete a conversation.

     Delete a conversation by `projectId` and `sessionId`.

    Args:
        project_id (int):
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteProjectConversationResponse200, DeleteProjectConversationResponse401, DeleteProjectConversationResponse404, DeleteProjectConversationResponse500]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        session_id=session_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: int,
    session_id: str,
    *,
    client: {},
) -> Optional[
    Union[
        DeleteProjectConversationResponse200,
        DeleteProjectConversationResponse401,
        DeleteProjectConversationResponse404,
        DeleteProjectConversationResponse500,
    ]
]:
    """Delete a conversation.

     Delete a conversation by `projectId` and `sessionId`.

    Args:
        project_id (int):
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteProjectConversationResponse200, DeleteProjectConversationResponse401, DeleteProjectConversationResponse404, DeleteProjectConversationResponse500]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            session_id=session_id,
            client=client,
        )
    ).parsed
