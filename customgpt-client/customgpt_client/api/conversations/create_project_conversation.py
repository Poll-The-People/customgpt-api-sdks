from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...models.create_project_conversation_json_body import CreateProjectConversationJsonBody
from ...models.create_project_conversation_response_201 import CreateProjectConversationResponse201
from ...models.create_project_conversation_response_401 import CreateProjectConversationResponse401
from ...models.create_project_conversation_response_404 import CreateProjectConversationResponse404
from ...models.create_project_conversation_response_500 import CreateProjectConversationResponse500
from ...types import Response


def _get_kwargs(
    project_id: int,
    *,
    client: {},
    json_body: CreateProjectConversationJsonBody,
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectId}/conversations".format(client.base_url, projectId=project_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(
    *, client: {}, response: httpx.Response
) -> Optional[
    Union[
        CreateProjectConversationResponse201,
        CreateProjectConversationResponse401,
        CreateProjectConversationResponse404,
        CreateProjectConversationResponse500,
    ]
]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CreateProjectConversationResponse201.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = CreateProjectConversationResponse401.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = CreateProjectConversationResponse404.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = CreateProjectConversationResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: {}, response: httpx.Response, content: Optional[bytes] = None
) -> Response[
    Union[
        CreateProjectConversationResponse201,
        CreateProjectConversationResponse401,
        CreateProjectConversationResponse404,
        CreateProjectConversationResponse500,
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
    *,
    client: {},
    json_body: CreateProjectConversationJsonBody,
):
    """Create a new conversation.

     Create a new conversation for a project by `projectId`.

    Args:
        project_id (int):
        json_body (CreateProjectConversationJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateProjectConversationResponse201, CreateProjectConversationResponse401, CreateProjectConversationResponse404, CreateProjectConversationResponse500]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
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
    *,
    client: {},
    json_body: CreateProjectConversationJsonBody,
) -> Optional[
    Union[
        CreateProjectConversationResponse201,
        CreateProjectConversationResponse401,
        CreateProjectConversationResponse404,
        CreateProjectConversationResponse500,
    ]
]:
    """Create a new conversation.

     Create a new conversation for a project by `projectId`.

    Args:
        project_id (int):
        json_body (CreateProjectConversationJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateProjectConversationResponse201, CreateProjectConversationResponse401, CreateProjectConversationResponse404, CreateProjectConversationResponse500]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    *,
    client: {},
    json_body: CreateProjectConversationJsonBody,
) -> Response[
    Union[
        CreateProjectConversationResponse201,
        CreateProjectConversationResponse401,
        CreateProjectConversationResponse404,
        CreateProjectConversationResponse500,
    ]
]:
    """Create a new conversation.

     Create a new conversation for a project by `projectId`.

    Args:
        project_id (int):
        json_body (CreateProjectConversationJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateProjectConversationResponse201, CreateProjectConversationResponse401, CreateProjectConversationResponse404, CreateProjectConversationResponse500]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: int,
    *,
    client: {},
    json_body: CreateProjectConversationJsonBody,
) -> Optional[
    Union[
        CreateProjectConversationResponse201,
        CreateProjectConversationResponse401,
        CreateProjectConversationResponse404,
        CreateProjectConversationResponse500,
    ]
]:
    """Create a new conversation.

     Create a new conversation for a project by `projectId`.

    Args:
        project_id (int):
        json_body (CreateProjectConversationJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateProjectConversationResponse201, CreateProjectConversationResponse401, CreateProjectConversationResponse404, CreateProjectConversationResponse500]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
