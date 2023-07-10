import json
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import requests

from ... import errors
from ...models.create_project_source_multipart_data import CreateProjectSourceMultipartData
from ...models.create_project_source_response_201 import CreateProjectSourceResponse201
from ...models.create_project_source_response_400 import CreateProjectSourceResponse400
from ...models.create_project_source_response_401 import CreateProjectSourceResponse401
from ...models.create_project_source_response_404 import CreateProjectSourceResponse404
from ...models.create_project_source_response_500 import CreateProjectSourceResponse500
from ...types import Response


def _get_kwargs(
    project_id: int,
    *,
    client: {},
    multipart_data: CreateProjectSourceMultipartData,
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectId}/sources".format(client.base_url, projectId=project_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "allow_redirects": client.follow_redirects,
        "files": multipart_multipart_data,
    }


def _parse_response(
    *, client: {}, response: None
) -> Optional[
    Union[
        CreateProjectSourceResponse201,
        CreateProjectSourceResponse400,
        CreateProjectSourceResponse401,
        CreateProjectSourceResponse404,
        CreateProjectSourceResponse500,
    ]
]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CreateProjectSourceResponse201.from_dict(json.loads(response.text))

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = CreateProjectSourceResponse400.from_dict(json.loads(response.text))

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = CreateProjectSourceResponse401.from_dict(json.loads(response.text))

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = CreateProjectSourceResponse404.from_dict(json.loads(response.text))

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = CreateProjectSourceResponse500.from_dict(json.loads(response.text))

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: {}, response: None, content: Optional[bytes] = None
) -> Response[
    Union[
        CreateProjectSourceResponse201,
        CreateProjectSourceResponse400,
        CreateProjectSourceResponse401,
        CreateProjectSourceResponse404,
        CreateProjectSourceResponse500,
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
    multipart_data: CreateProjectSourceMultipartData,
):
    """Create a new project source.

     Create a new source for a given project.

    Args:
        project_id (int):
        multipart_data (CreateProjectSourceMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateProjectSourceResponse201, CreateProjectSourceResponse400, CreateProjectSourceResponse401, CreateProjectSourceResponse404, CreateProjectSourceResponse500]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        multipart_data=multipart_data,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: int,
    *,
    client: {},
    multipart_data: CreateProjectSourceMultipartData,
) -> Optional[
    Union[
        CreateProjectSourceResponse201,
        CreateProjectSourceResponse400,
        CreateProjectSourceResponse401,
        CreateProjectSourceResponse404,
        CreateProjectSourceResponse500,
    ]
]:
    """Create a new project source.

     Create a new source for a given project.

    Args:
        project_id (int):
        multipart_data (CreateProjectSourceMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateProjectSourceResponse201, CreateProjectSourceResponse400, CreateProjectSourceResponse401, CreateProjectSourceResponse404, CreateProjectSourceResponse500]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    *,
    client: {},
    multipart_data: CreateProjectSourceMultipartData,
) -> Response[
    Union[
        CreateProjectSourceResponse201,
        CreateProjectSourceResponse400,
        CreateProjectSourceResponse401,
        CreateProjectSourceResponse404,
        CreateProjectSourceResponse500,
    ]
]:
    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        multipart_data=multipart_data,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: int,
    *,
    client: {},
    multipart_data: CreateProjectSourceMultipartData,
) -> Optional[
    Union[
        CreateProjectSourceResponse201,
        CreateProjectSourceResponse400,
        CreateProjectSourceResponse401,
        CreateProjectSourceResponse404,
        CreateProjectSourceResponse500,
    ]
]:
    """Create a new project source.

     Create a new source for a given project.

    Args:
        project_id (int):
        multipart_data (CreateProjectSourceMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateProjectSourceResponse201, CreateProjectSourceResponse400, CreateProjectSourceResponse401, CreateProjectSourceResponse404, CreateProjectSourceResponse500]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
