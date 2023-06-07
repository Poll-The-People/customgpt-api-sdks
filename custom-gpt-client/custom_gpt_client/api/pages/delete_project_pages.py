from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import CustomGPT, CustomGPTClient
from ...types import Response


def _get_kwargs(
    project_id: int,
    page_id: int,
    *,
    client: CustomGPT,
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectId}/pages/{pageId}".format(client.base_url, projectId=project_id, pageId=page_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: CustomGPTClient, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
        return None
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: CustomGPTClient, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: int,
    page_id: int,
    *,
    client: CustomGPT,
) -> Response[Any]:
    """Delete a certain page that belongs to a certain project.

     Delete a certain page of a specific project by `projectId` and `pageId`.

    Args:
        project_id (int):
        page_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        page_id=page_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    project_id: int,
    page_id: int,
    *,
    client: CustomGPT,
) -> Response[Any]:
    """Delete a certain page that belongs to a certain project.

     Delete a certain page of a specific project by `projectId` and `pageId`.

    Args:
        project_id (int):
        page_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        page_id=page_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
