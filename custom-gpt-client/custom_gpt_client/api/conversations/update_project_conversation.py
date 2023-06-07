from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import CustomGPT, CustomGPTClient
from ...models.update_project_conversation_json_body import UpdateProjectConversationJsonBody
from ...models.update_project_conversation_response_200 import UpdateProjectConversationResponse200
from ...types import Response


def _get_kwargs(
    project_id: int,
    session_id: str,
    *,
    client: CustomGPT,
    json_body: UpdateProjectConversationJsonBody,
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectId}/conversations/{sessionId}".format(
        client.base_url, projectId=project_id, sessionId=session_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(
    *, client: CustomGPTClient, response: httpx.Response
) -> Optional[Union[Any, UpdateProjectConversationResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UpdateProjectConversationResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: CustomGPTClient, response: httpx.Response
) -> Response[Union[Any, UpdateProjectConversationResponse200]]:
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
    json_body: UpdateProjectConversationJsonBody,
) -> Response[Union[Any, UpdateProjectConversationResponse200]]:
    """Update a conversation.

     Update a conversation by `projectId` and `sessionId`.

    Args:
        project_id (int):
        session_id (str):
        json_body (UpdateProjectConversationJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateProjectConversationResponse200]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        session_id=session_id,
        client=client,
        json_body=json_body,
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
    client: CustomGPT,
    json_body: UpdateProjectConversationJsonBody,
) -> Optional[Union[Any, UpdateProjectConversationResponse200]]:
    """Update a conversation.

     Update a conversation by `projectId` and `sessionId`.

    Args:
        project_id (int):
        session_id (str):
        json_body (UpdateProjectConversationJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateProjectConversationResponse200]
    """

    return sync_detailed(
        project_id=project_id,
        session_id=session_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    session_id: str,
    *,
    client: CustomGPT,
    json_body: UpdateProjectConversationJsonBody,
) -> Response[Union[Any, UpdateProjectConversationResponse200]]:
    """Update a conversation.

     Update a conversation by `projectId` and `sessionId`.

    Args:
        project_id (int):
        session_id (str):
        json_body (UpdateProjectConversationJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateProjectConversationResponse200]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        session_id=session_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: int,
    session_id: str,
    *,
    client: CustomGPT,
    json_body: UpdateProjectConversationJsonBody,
) -> Optional[Union[Any, UpdateProjectConversationResponse200]]:
    """Update a conversation.

     Update a conversation by `projectId` and `sessionId`.

    Args:
        project_id (int):
        session_id (str):
        json_body (UpdateProjectConversationJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateProjectConversationResponse200]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            session_id=session_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
