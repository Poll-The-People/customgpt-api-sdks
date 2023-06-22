from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...models.create_project_multipart_data import CreateProjectMultipartData
from ...models.create_project_response_201 import CreateProjectResponse201
from ...models.create_project_response_400 import CreateProjectResponse400
from ...models.create_project_response_401 import CreateProjectResponse401
from ...models.create_project_response_500 import CreateProjectResponse500
from ...types import Response


def _get_kwargs(
    *,
    client: {},
    multipart_data: CreateProjectMultipartData,
) -> Dict[str, Any]:
    url = "{}/api/v1/projects".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "files": multipart_multipart_data,
    }


def _parse_response(
    *, client: {}, response: httpx.Response
) -> Optional[
    Union[CreateProjectResponse201, CreateProjectResponse400, CreateProjectResponse401, CreateProjectResponse500]
]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CreateProjectResponse201.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = CreateProjectResponse400.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = CreateProjectResponse401.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = CreateProjectResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: {}, response: httpx.Response, content: Optional[bytes] = None
) -> Response[
    Union[CreateProjectResponse201, CreateProjectResponse400, CreateProjectResponse401, CreateProjectResponse500]
]:
    parse = _parse_response(client=client, response=response)
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content if content is None else content,
        headers=response.headers,
        parsed=parse,
    )


def sync_detailed(
    *,
    client: {},
    multipart_data: CreateProjectMultipartData,
):
    """Create a new project.

     Create a new project from either sitemap or uploaded file.

    Args:
        multipart_data (CreateProjectMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateProjectResponse201, CreateProjectResponse400, CreateProjectResponse401, CreateProjectResponse500]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: {},
    multipart_data: CreateProjectMultipartData,
) -> Optional[
    Union[CreateProjectResponse201, CreateProjectResponse400, CreateProjectResponse401, CreateProjectResponse500]
]:
    """Create a new project.

     Create a new project from either sitemap or uploaded file.

    Args:
        multipart_data (CreateProjectMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateProjectResponse201, CreateProjectResponse400, CreateProjectResponse401, CreateProjectResponse500]
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: {},
    multipart_data: CreateProjectMultipartData,
) -> Response[
    Union[CreateProjectResponse201, CreateProjectResponse400, CreateProjectResponse401, CreateProjectResponse500]
]:
    """Create a new project.

     Create a new project from either sitemap or uploaded file.

    Args:
        multipart_data (CreateProjectMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateProjectResponse201, CreateProjectResponse400, CreateProjectResponse401, CreateProjectResponse500]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: {},
    multipart_data: CreateProjectMultipartData,
) -> Optional[
    Union[CreateProjectResponse201, CreateProjectResponse400, CreateProjectResponse401, CreateProjectResponse500]
]:
    """Create a new project.

     Create a new project from either sitemap or uploaded file.

    Args:
        multipart_data (CreateProjectMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateProjectResponse201, CreateProjectResponse400, CreateProjectResponse401, CreateProjectResponse500]
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
