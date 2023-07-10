import json
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import requests

from ... import errors
from ...models.create_project_plugin_json_body import CreateProjectPluginJsonBody
from ...models.create_project_plugin_response_201 import CreateProjectPluginResponse201
from ...models.create_project_plugin_response_401 import CreateProjectPluginResponse401
from ...models.create_project_plugin_response_404 import CreateProjectPluginResponse404
from ...models.create_project_plugin_response_500 import CreateProjectPluginResponse500
from ...types import Response


def _get_kwargs(
    project_id: int,
    *,
    client: {},
    json_body: CreateProjectPluginJsonBody,
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectId}/plugins".format(client.base_url, projectId=project_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "allow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(
    *, client: {}, response: None
) -> Optional[
    Union[
        CreateProjectPluginResponse201,
        CreateProjectPluginResponse401,
        CreateProjectPluginResponse404,
        CreateProjectPluginResponse500,
    ]
]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CreateProjectPluginResponse201.from_dict(json.loads(response.text))

        return response_201
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = CreateProjectPluginResponse401.from_dict(json.loads(response.text))

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = CreateProjectPluginResponse404.from_dict(json.loads(response.text))

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = CreateProjectPluginResponse500.from_dict(json.loads(response.text))

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: {}, response: None, content: Optional[bytes] = None
) -> Response[
    Union[
        CreateProjectPluginResponse201,
        CreateProjectPluginResponse401,
        CreateProjectPluginResponse404,
        CreateProjectPluginResponse500,
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
    json_body: CreateProjectPluginJsonBody,
):
    """Create a plugin.

     Create a new plugin for a specific project by `projectId`.

    Args:
        project_id (int):
        json_body (CreateProjectPluginJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateProjectPluginResponse201, CreateProjectPluginResponse401, CreateProjectPluginResponse404, CreateProjectPluginResponse500]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        json_body=json_body,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: int,
    *,
    client: {},
    json_body: CreateProjectPluginJsonBody,
) -> Optional[
    Union[
        CreateProjectPluginResponse201,
        CreateProjectPluginResponse401,
        CreateProjectPluginResponse404,
        CreateProjectPluginResponse500,
    ]
]:
    """Create a plugin.

     Create a new plugin for a specific project by `projectId`.

    Args:
        project_id (int):
        json_body (CreateProjectPluginJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateProjectPluginResponse201, CreateProjectPluginResponse401, CreateProjectPluginResponse404, CreateProjectPluginResponse500]
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
    json_body: CreateProjectPluginJsonBody,
) -> Response[
    Union[
        CreateProjectPluginResponse201,
        CreateProjectPluginResponse401,
        CreateProjectPluginResponse404,
        CreateProjectPluginResponse500,
    ]
]:
    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        json_body=json_body,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: int,
    *,
    client: {},
    json_body: CreateProjectPluginJsonBody,
) -> Optional[
    Union[
        CreateProjectPluginResponse201,
        CreateProjectPluginResponse401,
        CreateProjectPluginResponse404,
        CreateProjectPluginResponse500,
    ]
]:
    """Create a plugin.

     Create a new plugin for a specific project by `projectId`.

    Args:
        project_id (int):
        json_body (CreateProjectPluginJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateProjectPluginResponse201, CreateProjectPluginResponse401, CreateProjectPluginResponse404, CreateProjectPluginResponse500]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
