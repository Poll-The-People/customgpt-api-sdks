from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...models.stats_project_response_200 import StatsProjectResponse200
from ...models.stats_project_response_401 import StatsProjectResponse401
from ...models.stats_project_response_404 import StatsProjectResponse404
from ...models.stats_project_response_500 import StatsProjectResponse500
from ...types import Response


def _get_kwargs(
    project_id: int,
    *,
    client: {},
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectId}/stats".format(client.base_url, projectId=project_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(
    *, client: {}, response: httpx.Response
) -> Optional[
    Union[StatsProjectResponse200, StatsProjectResponse401, StatsProjectResponse404, StatsProjectResponse500]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = StatsProjectResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = StatsProjectResponse401.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = StatsProjectResponse404.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = StatsProjectResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: {}, response: httpx.Response, content: Optional[bytes] = None
) -> Response[
    Union[StatsProjectResponse200, StatsProjectResponse401, StatsProjectResponse404, StatsProjectResponse500]
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
):
    """Get the stats for a certain project.

     Get the stats for a project by `projectId`.

    Args:
        project_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[StatsProjectResponse200, StatsProjectResponse401, StatsProjectResponse404, StatsProjectResponse500]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
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
) -> Optional[
    Union[StatsProjectResponse200, StatsProjectResponse401, StatsProjectResponse404, StatsProjectResponse500]
]:
    """Get the stats for a certain project.

     Get the stats for a project by `projectId`.

    Args:
        project_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[StatsProjectResponse200, StatsProjectResponse401, StatsProjectResponse404, StatsProjectResponse500]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    *,
    client: {},
) -> Response[
    Union[StatsProjectResponse200, StatsProjectResponse401, StatsProjectResponse404, StatsProjectResponse500]
]:
    """Get the stats for a certain project.

     Get the stats for a project by `projectId`.

    Args:
        project_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[StatsProjectResponse200, StatsProjectResponse401, StatsProjectResponse404, StatsProjectResponse500]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: int,
    *,
    client: {},
) -> Optional[
    Union[StatsProjectResponse200, StatsProjectResponse401, StatsProjectResponse404, StatsProjectResponse500]
]:
    """Get the stats for a certain project.

     Get the stats for a project by `projectId`.

    Args:
        project_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[StatsProjectResponse200, StatsProjectResponse401, StatsProjectResponse404, StatsProjectResponse500]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
        )
    ).parsed
