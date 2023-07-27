import json
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import requests

from ... import errors
from ...models.create_source_multipart_data import CreateSourceMultipartData
from ...models.create_source_response_201 import CreateSourceResponse201
from ...models.create_source_response_400 import CreateSourceResponse400
from ...models.create_source_response_401 import CreateSourceResponse401
from ...models.create_source_response_404 import CreateSourceResponse404
from ...models.create_source_response_500 import CreateSourceResponse500
from ...types import Response


def _get_kwargs(
    project_id: int,
    *,
    client: {},
    multipart_data: CreateSourceMultipartData,
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
        CreateSourceResponse201,
        CreateSourceResponse400,
        CreateSourceResponse401,
        CreateSourceResponse404,
        CreateSourceResponse500,
    ]
]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CreateSourceResponse201.from_dict(json.loads(response.text))

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = CreateSourceResponse400.from_dict(json.loads(response.text))

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = CreateSourceResponse401.from_dict(json.loads(response.text))

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = CreateSourceResponse404.from_dict(json.loads(response.text))

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = CreateSourceResponse500.from_dict(json.loads(response.text))

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: {}, response: None, content: Optional[bytes] = None
) -> Response[
    Union[
        CreateSourceResponse201,
        CreateSourceResponse400,
        CreateSourceResponse401,
        CreateSourceResponse404,
        CreateSourceResponse500,
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
    multipart_data: CreateSourceMultipartData,
):
    """Create a new project source.

     Create a new data source for a given project, allowing you to add additional context by specifying a
    sitemap URL or uploading a file. This endpoint enables you to enrich the project's information by
    incorporating relevant data sources.
    Here is an example to add a new source to project: [API](https://github.com/Poll-The-
    People/customgpt-cookbook/blob/main/examples/Add_a_sitemap_to_an_existing_project.ipynb)
    [SDK](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/SDK_Add_a_Sitemap_to_project.ipynb).

    Args:
        project_id (int):
        multipart_data (CreateSourceMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateSourceResponse201, CreateSourceResponse400, CreateSourceResponse401, CreateSourceResponse404, CreateSourceResponse500]]
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
    multipart_data: CreateSourceMultipartData,
) -> Optional[
    Union[
        CreateSourceResponse201,
        CreateSourceResponse400,
        CreateSourceResponse401,
        CreateSourceResponse404,
        CreateSourceResponse500,
    ]
]:
    """Create a new project source.

     Create a new data source for a given project, allowing you to add additional context by specifying a
    sitemap URL or uploading a file. This endpoint enables you to enrich the project's information by
    incorporating relevant data sources.
    Here is an example to add a new source to project: [API](https://github.com/Poll-The-
    People/customgpt-cookbook/blob/main/examples/Add_a_sitemap_to_an_existing_project.ipynb)
    [SDK](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/SDK_Add_a_Sitemap_to_project.ipynb).

    Args:
        project_id (int):
        multipart_data (CreateSourceMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateSourceResponse201, CreateSourceResponse400, CreateSourceResponse401, CreateSourceResponse404, CreateSourceResponse500]
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
    multipart_data: CreateSourceMultipartData,
) -> Response[
    Union[
        CreateSourceResponse201,
        CreateSourceResponse400,
        CreateSourceResponse401,
        CreateSourceResponse404,
        CreateSourceResponse500,
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
    multipart_data: CreateSourceMultipartData,
) -> Optional[
    Union[
        CreateSourceResponse201,
        CreateSourceResponse400,
        CreateSourceResponse401,
        CreateSourceResponse404,
        CreateSourceResponse500,
    ]
]:
    """Create a new project source.

     Create a new data source for a given project, allowing you to add additional context by specifying a
    sitemap URL or uploading a file. This endpoint enables you to enrich the project's information by
    incorporating relevant data sources.
    Here is an example to add a new source to project: [API](https://github.com/Poll-The-
    People/customgpt-cookbook/blob/main/examples/Add_a_sitemap_to_an_existing_project.ipynb)
    [SDK](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/SDK_Add_a_Sitemap_to_project.ipynb).

    Args:
        project_id (int):
        multipart_data (CreateSourceMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateSourceResponse201, CreateSourceResponse400, CreateSourceResponse401, CreateSourceResponse404, CreateSourceResponse500]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
