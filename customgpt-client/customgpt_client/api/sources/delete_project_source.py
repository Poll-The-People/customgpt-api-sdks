import json
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import requests

from ... import errors
from ...models.delete_project_source_response_200 import DeleteProjectSourceResponse200
from ...models.delete_project_source_response_401 import DeleteProjectSourceResponse401
from ...models.delete_project_source_response_404 import DeleteProjectSourceResponse404
from ...models.delete_project_source_response_500 import DeleteProjectSourceResponse500
from ...types import Response


def _get_kwargs(
    project_id: int,
    source_id: int,
    *,
    client: {},
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectId}/sources/{sourceId}".format(
        client.base_url, projectId=project_id, sourceId=source_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "allow_redirects": client.follow_redirects,
    }


def _parse_response(
    *, client: {}, response: None
) -> Optional[
    Union[
        DeleteProjectSourceResponse200,
        DeleteProjectSourceResponse401,
        DeleteProjectSourceResponse404,
        DeleteProjectSourceResponse500,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DeleteProjectSourceResponse200.from_dict(json.loads(response.text))

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = DeleteProjectSourceResponse401.from_dict(json.loads(response.text))

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = DeleteProjectSourceResponse404.from_dict(json.loads(response.text))

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = DeleteProjectSourceResponse500.from_dict(json.loads(response.text))

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: {}, response: None, content: Optional[bytes] = None
) -> Response[
    Union[
        DeleteProjectSourceResponse200,
        DeleteProjectSourceResponse401,
        DeleteProjectSourceResponse404,
        DeleteProjectSourceResponse500,
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
    source_id: int,
    *,
    client: {},
):
    """Delete a project source.

     Delete a source for a given project.

    Args:
        project_id (int):
        source_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteProjectSourceResponse200, DeleteProjectSourceResponse401, DeleteProjectSourceResponse404, DeleteProjectSourceResponse500]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        source_id=source_id,
        client=client,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: int,
    source_id: int,
    *,
    client: {},
) -> Optional[
    Union[
        DeleteProjectSourceResponse200,
        DeleteProjectSourceResponse401,
        DeleteProjectSourceResponse404,
        DeleteProjectSourceResponse500,
    ]
]:
    """Delete a project source.

     Delete a source for a given project.

    Args:
        project_id (int):
        source_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteProjectSourceResponse200, DeleteProjectSourceResponse401, DeleteProjectSourceResponse404, DeleteProjectSourceResponse500]
    """

    return sync_detailed(
        project_id=project_id,
        source_id=source_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    source_id: int,
    *,
    client: {},
) -> Response[
    Union[
        DeleteProjectSourceResponse200,
        DeleteProjectSourceResponse401,
        DeleteProjectSourceResponse404,
        DeleteProjectSourceResponse500,
    ]
]:
    kwargs = _get_kwargs(
        project_id=project_id,
        source_id=source_id,
        client=client,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: int,
    source_id: int,
    *,
    client: {},
) -> Optional[
    Union[
        DeleteProjectSourceResponse200,
        DeleteProjectSourceResponse401,
        DeleteProjectSourceResponse404,
        DeleteProjectSourceResponse500,
    ]
]:
    """Delete a project source.

     Delete a source for a given project.

    Args:
        project_id (int):
        source_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteProjectSourceResponse200, DeleteProjectSourceResponse401, DeleteProjectSourceResponse404, DeleteProjectSourceResponse500]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            source_id=source_id,
            client=client,
        )
    ).parsed
