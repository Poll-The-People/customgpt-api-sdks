from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...models.get_project_pages_order import GetProjectPagesOrder
from ...models.get_project_pages_response_200 import GetProjectPagesResponse200
from ...models.get_project_pages_response_401 import GetProjectPagesResponse401
from ...models.get_project_pages_response_404 import GetProjectPagesResponse404
from ...models.get_project_pages_response_500 import GetProjectPagesResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: int,
    *,
    client: {},
    page: Union[Unset, None, int] = 1,
    duration: Union[Unset, None, int] = 90,
    order: Union[Unset, None, GetProjectPagesOrder] = GetProjectPagesOrder.DESC,
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectId}/pages".format(client.base_url, projectId=project_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["duration"] = duration

    json_order: Union[Unset, None, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value if order else None

    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(
    *, client: {}, response: httpx.Response
) -> Optional[
    Union[
        GetProjectPagesResponse200, GetProjectPagesResponse401, GetProjectPagesResponse404, GetProjectPagesResponse500
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetProjectPagesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetProjectPagesResponse401.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetProjectPagesResponse404.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetProjectPagesResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: {}, response: httpx.Response, content: Optional[bytes] = None
) -> Response[
    Union[
        GetProjectPagesResponse200, GetProjectPagesResponse401, GetProjectPagesResponse404, GetProjectPagesResponse500
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
    page: Union[Unset, None, int] = 1,
    duration: Union[Unset, None, int] = 90,
    order: Union[Unset, None, GetProjectPagesOrder] = GetProjectPagesOrder.DESC,
):
    """List all pages that belong to a project.

     Get a list of all pages that belong to a project.

    Args:
        project_id (int):  Example: 1.
        page (Union[Unset, None, int]):  Default: 1.
        duration (Union[Unset, None, int]):  Default: 90.
        order (Union[Unset, None, GetProjectPagesOrder]):  Default: GetProjectPagesOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetProjectPagesResponse200, GetProjectPagesResponse401, GetProjectPagesResponse404, GetProjectPagesResponse500]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        page=page,
        duration=duration,
        order=order,
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
    page: Union[Unset, None, int] = 1,
    duration: Union[Unset, None, int] = 90,
    order: Union[Unset, None, GetProjectPagesOrder] = GetProjectPagesOrder.DESC,
) -> Optional[
    Union[
        GetProjectPagesResponse200, GetProjectPagesResponse401, GetProjectPagesResponse404, GetProjectPagesResponse500
    ]
]:
    """List all pages that belong to a project.

     Get a list of all pages that belong to a project.

    Args:
        project_id (int):  Example: 1.
        page (Union[Unset, None, int]):  Default: 1.
        duration (Union[Unset, None, int]):  Default: 90.
        order (Union[Unset, None, GetProjectPagesOrder]):  Default: GetProjectPagesOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetProjectPagesResponse200, GetProjectPagesResponse401, GetProjectPagesResponse404, GetProjectPagesResponse500]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        page=page,
        duration=duration,
        order=order,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    *,
    client: {},
    page: Union[Unset, None, int] = 1,
    duration: Union[Unset, None, int] = 90,
    order: Union[Unset, None, GetProjectPagesOrder] = GetProjectPagesOrder.DESC,
) -> Response[
    Union[
        GetProjectPagesResponse200, GetProjectPagesResponse401, GetProjectPagesResponse404, GetProjectPagesResponse500
    ]
]:
    """List all pages that belong to a project.

     Get a list of all pages that belong to a project.

    Args:
        project_id (int):  Example: 1.
        page (Union[Unset, None, int]):  Default: 1.
        duration (Union[Unset, None, int]):  Default: 90.
        order (Union[Unset, None, GetProjectPagesOrder]):  Default: GetProjectPagesOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetProjectPagesResponse200, GetProjectPagesResponse401, GetProjectPagesResponse404, GetProjectPagesResponse500]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        page=page,
        duration=duration,
        order=order,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: int,
    *,
    client: {},
    page: Union[Unset, None, int] = 1,
    duration: Union[Unset, None, int] = 90,
    order: Union[Unset, None, GetProjectPagesOrder] = GetProjectPagesOrder.DESC,
) -> Optional[
    Union[
        GetProjectPagesResponse200, GetProjectPagesResponse401, GetProjectPagesResponse404, GetProjectPagesResponse500
    ]
]:
    """List all pages that belong to a project.

     Get a list of all pages that belong to a project.

    Args:
        project_id (int):  Example: 1.
        page (Union[Unset, None, int]):  Default: 1.
        duration (Union[Unset, None, int]):  Default: 90.
        order (Union[Unset, None, GetProjectPagesOrder]):  Default: GetProjectPagesOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetProjectPagesResponse200, GetProjectPagesResponse401, GetProjectPagesResponse404, GetProjectPagesResponse500]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            page=page,
            duration=duration,
            order=order,
        )
    ).parsed
