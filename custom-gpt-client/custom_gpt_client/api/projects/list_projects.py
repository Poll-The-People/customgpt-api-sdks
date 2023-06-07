from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import CustomGPT, CustomGPTClient
from ...models.list_projects_order import ListProjectsOrder
from ...models.list_projects_response_200 import ListProjectsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: CustomGPT,
    page: Union[Unset, None, int] = 1,
    duration: Union[Unset, None, int] = 90,
    order: Union[Unset, None, ListProjectsOrder] = ListProjectsOrder.DESC,
    width: Union[Unset, None, str] = "100%",
    height: Union[Unset, None, str] = "auto",
) -> Dict[str, Any]:
    url = "{}/api/v1/projects".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["duration"] = duration

    json_order: Union[Unset, None, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value if order else None

    params["order"] = json_order

    params["width"] = width

    params["height"] = height

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
    *, client: CustomGPTClient, response: httpx.Response
) -> Optional[Union[Any, ListProjectsResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListProjectsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: CustomGPTClient, response: httpx.Response
) -> Response[Union[Any, ListProjectsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: CustomGPT,
    page: Union[Unset, None, int] = 1,
    duration: Union[Unset, None, int] = 90,
    order: Union[Unset, None, ListProjectsOrder] = ListProjectsOrder.DESC,
    width: Union[Unset, None, str] = "100%",
    height: Union[Unset, None, str] = "auto",
) -> Response[Union[Any, ListProjectsResponse200]]:
    """List all projects.

     Get a list of all projects that belong to the user.

    Args:
        page (Union[Unset, None, int]):  Default: 1.
        duration (Union[Unset, None, int]):  Default: 90.
        order (Union[Unset, None, ListProjectsOrder]):  Default: ListProjectsOrder.DESC.
        width (Union[Unset, None, str]):  Default: '100%'. Example: 50rem.
        height (Union[Unset, None, str]):  Default: 'auto'. Example: 50rem.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListProjectsResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        duration=duration,
        order=order,
        width=width,
        height=height,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: CustomGPT,
    page: Union[Unset, None, int] = 1,
    duration: Union[Unset, None, int] = 90,
    order: Union[Unset, None, ListProjectsOrder] = ListProjectsOrder.DESC,
    width: Union[Unset, None, str] = "100%",
    height: Union[Unset, None, str] = "auto",
) -> Optional[Union[Any, ListProjectsResponse200]]:
    """List all projects.

     Get a list of all projects that belong to the user.

    Args:
        page (Union[Unset, None, int]):  Default: 1.
        duration (Union[Unset, None, int]):  Default: 90.
        order (Union[Unset, None, ListProjectsOrder]):  Default: ListProjectsOrder.DESC.
        width (Union[Unset, None, str]):  Default: '100%'. Example: 50rem.
        height (Union[Unset, None, str]):  Default: 'auto'. Example: 50rem.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListProjectsResponse200]
    """

    return sync_detailed(
        client=client,
        page=page,
        duration=duration,
        order=order,
        width=width,
        height=height,
    ).parsed


async def asyncio_detailed(
    *,
    client: CustomGPT,
    page: Union[Unset, None, int] = 1,
    duration: Union[Unset, None, int] = 90,
    order: Union[Unset, None, ListProjectsOrder] = ListProjectsOrder.DESC,
    width: Union[Unset, None, str] = "100%",
    height: Union[Unset, None, str] = "auto",
) -> Response[Union[Any, ListProjectsResponse200]]:
    """List all projects.

     Get a list of all projects that belong to the user.

    Args:
        page (Union[Unset, None, int]):  Default: 1.
        duration (Union[Unset, None, int]):  Default: 90.
        order (Union[Unset, None, ListProjectsOrder]):  Default: ListProjectsOrder.DESC.
        width (Union[Unset, None, str]):  Default: '100%'. Example: 50rem.
        height (Union[Unset, None, str]):  Default: 'auto'. Example: 50rem.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListProjectsResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        duration=duration,
        order=order,
        width=width,
        height=height,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: CustomGPT,
    page: Union[Unset, None, int] = 1,
    duration: Union[Unset, None, int] = 90,
    order: Union[Unset, None, ListProjectsOrder] = ListProjectsOrder.DESC,
    width: Union[Unset, None, str] = "100%",
    height: Union[Unset, None, str] = "auto",
) -> Optional[Union[Any, ListProjectsResponse200]]:
    """List all projects.

     Get a list of all projects that belong to the user.

    Args:
        page (Union[Unset, None, int]):  Default: 1.
        duration (Union[Unset, None, int]):  Default: 90.
        order (Union[Unset, None, ListProjectsOrder]):  Default: ListProjectsOrder.DESC.
        width (Union[Unset, None, str]):  Default: '100%'. Example: 50rem.
        height (Union[Unset, None, str]):  Default: 'auto'. Example: 50rem.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListProjectsResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            duration=duration,
            order=order,
            width=width,
            height=height,
        )
    ).parsed
