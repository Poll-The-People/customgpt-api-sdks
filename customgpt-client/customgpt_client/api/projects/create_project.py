import json
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import requests

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
        "allow_redirects": client.follow_redirects,
        "files": multipart_multipart_data,
    }


def _parse_response(
    *, client: {}, response: None
) -> Optional[
    Union[CreateProjectResponse201, CreateProjectResponse400, CreateProjectResponse401, CreateProjectResponse500]
]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CreateProjectResponse201.from_dict(json.loads(response.text))

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = CreateProjectResponse400.from_dict(json.loads(response.text))

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = CreateProjectResponse401.from_dict(json.loads(response.text))

        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = CreateProjectResponse500.from_dict(json.loads(response.text))

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: {}, response: None, content: Optional[bytes] = None
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

     Create a new project by importing data either from a sitemap or an uploaded file. This endpoint
    enables you to initiate the creation of a new project by supplying the necessary project data that
    will be used as the context. You can choose to import the project structure and content from a
    sitemap url or upload a specific file format that contains the context can be any text, audio or
    video format. The system will process the provided data and generate a new project based on the
    imported or uploaded information.
    Here is an example to create a bot using a sitemap: [API](https://github.com/Poll-The-
    People/customgpt-cookbook/blob/main/examples/Create_Bot_By_Sitemap.ipynb)
    [SDK](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/SDK_Create_Bot_By_Sitemap.ipynb).

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

    response = requests.request(
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

     Create a new project by importing data either from a sitemap or an uploaded file. This endpoint
    enables you to initiate the creation of a new project by supplying the necessary project data that
    will be used as the context. You can choose to import the project structure and content from a
    sitemap url or upload a specific file format that contains the context can be any text, audio or
    video format. The system will process the provided data and generate a new project based on the
    imported or uploaded information.
    Here is an example to create a bot using a sitemap: [API](https://github.com/Poll-The-
    People/customgpt-cookbook/blob/main/examples/Create_Bot_By_Sitemap.ipynb)
    [SDK](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/SDK_Create_Bot_By_Sitemap.ipynb).

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
    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: {},
    multipart_data: CreateProjectMultipartData,
) -> Optional[
    Union[CreateProjectResponse201, CreateProjectResponse400, CreateProjectResponse401, CreateProjectResponse500]
]:
    """Create a new project.

     Create a new project by importing data either from a sitemap or an uploaded file. This endpoint
    enables you to initiate the creation of a new project by supplying the necessary project data that
    will be used as the context. You can choose to import the project structure and content from a
    sitemap url or upload a specific file format that contains the context can be any text, audio or
    video format. The system will process the provided data and generate a new project based on the
    imported or uploaded information.
    Here is an example to create a bot using a sitemap: [API](https://github.com/Poll-The-
    People/customgpt-cookbook/blob/main/examples/Create_Bot_By_Sitemap.ipynb)
    [SDK](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/SDK_Create_Bot_By_Sitemap.ipynb).

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
