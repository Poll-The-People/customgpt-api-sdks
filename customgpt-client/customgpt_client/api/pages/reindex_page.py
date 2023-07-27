import json
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import requests

from ... import errors
from ...models.reindex_page_response_200 import ReindexPageResponse200
from ...models.reindex_page_response_400 import ReindexPageResponse400
from ...models.reindex_page_response_401 import ReindexPageResponse401
from ...models.reindex_page_response_403 import ReindexPageResponse403
from ...models.reindex_page_response_500 import ReindexPageResponse500
from ...types import Response


def _get_kwargs(
    project_id: int,
    page_id: int,
    *,
    client: {},
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectId}/pages/{pageId}/reindex".format(
        client.base_url, projectId=project_id, pageId=page_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
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
        ReindexPageResponse200,
        ReindexPageResponse400,
        ReindexPageResponse401,
        ReindexPageResponse403,
        ReindexPageResponse500,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ReindexPageResponse200.from_dict(json.loads(response.text))

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ReindexPageResponse400.from_dict(json.loads(response.text))

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ReindexPageResponse401.from_dict(json.loads(response.text))

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ReindexPageResponse403.from_dict(json.loads(response.text))

        return response_403
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ReindexPageResponse500.from_dict(json.loads(response.text))

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: {}, response: None, content: Optional[bytes] = None
) -> Response[
    Union[
        ReindexPageResponse200,
        ReindexPageResponse400,
        ReindexPageResponse401,
        ReindexPageResponse403,
        ReindexPageResponse500,
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
    page_id: int,
    *,
    client: {},
):
    """Reindex a certain page that belongs to a certain project.

     Reindex a specific page within a project based on its unique projectId and pageId. This endpoint
    allows you to refresh a particular page from the project. Our system will crawl and index page
    content newly.

    Args:
        project_id (int):
        page_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ReindexPageResponse200, ReindexPageResponse400, ReindexPageResponse401, ReindexPageResponse403, ReindexPageResponse500]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        page_id=page_id,
        client=client,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: int,
    page_id: int,
    *,
    client: {},
) -> Optional[
    Union[
        ReindexPageResponse200,
        ReindexPageResponse400,
        ReindexPageResponse401,
        ReindexPageResponse403,
        ReindexPageResponse500,
    ]
]:
    """Reindex a certain page that belongs to a certain project.

     Reindex a specific page within a project based on its unique projectId and pageId. This endpoint
    allows you to refresh a particular page from the project. Our system will crawl and index page
    content newly.

    Args:
        project_id (int):
        page_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ReindexPageResponse200, ReindexPageResponse400, ReindexPageResponse401, ReindexPageResponse403, ReindexPageResponse500]
    """

    return sync_detailed(
        project_id=project_id,
        page_id=page_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    page_id: int,
    *,
    client: {},
) -> Response[
    Union[
        ReindexPageResponse200,
        ReindexPageResponse400,
        ReindexPageResponse401,
        ReindexPageResponse403,
        ReindexPageResponse500,
    ]
]:
    kwargs = _get_kwargs(
        project_id=project_id,
        page_id=page_id,
        client=client,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: int,
    page_id: int,
    *,
    client: {},
) -> Optional[
    Union[
        ReindexPageResponse200,
        ReindexPageResponse400,
        ReindexPageResponse401,
        ReindexPageResponse403,
        ReindexPageResponse500,
    ]
]:
    """Reindex a certain page that belongs to a certain project.

     Reindex a specific page within a project based on its unique projectId and pageId. This endpoint
    allows you to refresh a particular page from the project. Our system will crawl and index page
    content newly.

    Args:
        project_id (int):
        page_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ReindexPageResponse200, ReindexPageResponse400, ReindexPageResponse401, ReindexPageResponse403, ReindexPageResponse500]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            page_id=page_id,
            client=client,
        )
    ).parsed
