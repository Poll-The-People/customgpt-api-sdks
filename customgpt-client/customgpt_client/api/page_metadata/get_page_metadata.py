import json
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import requests

from ... import errors
from ...models.get_page_metadata_response_200 import GetPageMetadataResponse200
from ...models.get_page_metadata_response_400 import GetPageMetadataResponse400
from ...models.get_page_metadata_response_401 import GetPageMetadataResponse401
from ...models.get_page_metadata_response_404 import GetPageMetadataResponse404
from ...types import Response


def _get_kwargs(
    project_id: int,
    page_id: str,
    *,
    client: {},
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectId}/pages/{pageId}/metadata".format(
        client.base_url, projectId=project_id, pageId=page_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
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
        GetPageMetadataResponse200, GetPageMetadataResponse400, GetPageMetadataResponse401, GetPageMetadataResponse404
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetPageMetadataResponse200.from_dict(json.loads(response.text))

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetPageMetadataResponse400.from_dict(json.loads(response.text))

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetPageMetadataResponse401.from_dict(json.loads(response.text))

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetPageMetadataResponse404.from_dict(json.loads(response.text))

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: {}, response: None, content: Optional[bytes] = None
) -> Response[
    Union[
        GetPageMetadataResponse200, GetPageMetadataResponse400, GetPageMetadataResponse401, GetPageMetadataResponse404
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
    page_id: str,
    *,
    client: {},
):
    """Get the Metadata for a certain page.

     Retrieve the Metadata for a page based on its unique identifier. This endpoint allows you to fetch
    the metadata associated with a specific page.

    Args:
        project_id (int):
        page_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetPageMetadataResponse200, GetPageMetadataResponse400, GetPageMetadataResponse401, GetPageMetadataResponse404]]
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
    page_id: str,
    *,
    client: {},
) -> Optional[
    Union[
        GetPageMetadataResponse200, GetPageMetadataResponse400, GetPageMetadataResponse401, GetPageMetadataResponse404
    ]
]:
    """Get the Metadata for a certain page.

     Retrieve the Metadata for a page based on its unique identifier. This endpoint allows you to fetch
    the metadata associated with a specific page.

    Args:
        project_id (int):
        page_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetPageMetadataResponse200, GetPageMetadataResponse400, GetPageMetadataResponse401, GetPageMetadataResponse404]
    """

    return sync_detailed(
        project_id=project_id,
        page_id=page_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    page_id: str,
    *,
    client: {},
) -> Response[
    Union[
        GetPageMetadataResponse200, GetPageMetadataResponse400, GetPageMetadataResponse401, GetPageMetadataResponse404
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
    page_id: str,
    *,
    client: {},
) -> Optional[
    Union[
        GetPageMetadataResponse200, GetPageMetadataResponse400, GetPageMetadataResponse401, GetPageMetadataResponse404
    ]
]:
    """Get the Metadata for a certain page.

     Retrieve the Metadata for a page based on its unique identifier. This endpoint allows you to fetch
    the metadata associated with a specific page.

    Args:
        project_id (int):
        page_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetPageMetadataResponse200, GetPageMetadataResponse400, GetPageMetadataResponse401, GetPageMetadataResponse404]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            page_id=page_id,
            client=client,
        )
    ).parsed
