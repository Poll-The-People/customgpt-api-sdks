from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...models.get_project_response_200 import GetProjectResponse200
from ...models.get_project_response_401 import GetProjectResponse401
from ...models.get_project_response_404 import GetProjectResponse404
from ...models.get_project_response_500 import GetProjectResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: int,
    *,
    client: {},
    width: Union[Unset, None, str] = "100%",
    height: Union[Unset, None, str] = "auto",
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectId}".format(client.base_url, projectId=project_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
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
    *, client: {}, response: httpx.Response
) -> Optional[Union[GetProjectResponse200, GetProjectResponse401, GetProjectResponse404, GetProjectResponse500]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetProjectResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetProjectResponse401.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetProjectResponse404.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetProjectResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: {}, response: httpx.Response, content: Optional[bytes] = None
) -> Response[Union[GetProjectResponse200, GetProjectResponse401, GetProjectResponse404, GetProjectResponse500]]:
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
    width: Union[Unset, None, str] = "100%",
    height: Union[Unset, None, str] = "auto",
):
    """Show a certain project.

     View a specific project by project ID.

    Args:
        project_id (int):  Example: 1.
        width (Union[Unset, None, str]):  Default: '100%'. Example: 50rem.
        height (Union[Unset, None, str]):  Default: 'auto'. Example: 50rem.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetProjectResponse200, GetProjectResponse401, GetProjectResponse404, GetProjectResponse500]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        width=width,
        height=height,
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
    width: Union[Unset, None, str] = "100%",
    height: Union[Unset, None, str] = "auto",
) -> Optional[Union[GetProjectResponse200, GetProjectResponse401, GetProjectResponse404, GetProjectResponse500]]:
    """Show a certain project.

     View a specific project by project ID.

    Args:
        project_id (int):  Example: 1.
        width (Union[Unset, None, str]):  Default: '100%'. Example: 50rem.
        height (Union[Unset, None, str]):  Default: 'auto'. Example: 50rem.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetProjectResponse200, GetProjectResponse401, GetProjectResponse404, GetProjectResponse500]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        width=width,
        height=height,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    *,
    client: {},
    width: Union[Unset, None, str] = "100%",
    height: Union[Unset, None, str] = "auto",
) -> Response[Union[GetProjectResponse200, GetProjectResponse401, GetProjectResponse404, GetProjectResponse500]]:
    """Show a certain project.

     View a specific project by project ID.

    Args:
        project_id (int):  Example: 1.
        width (Union[Unset, None, str]):  Default: '100%'. Example: 50rem.
        height (Union[Unset, None, str]):  Default: 'auto'. Example: 50rem.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetProjectResponse200, GetProjectResponse401, GetProjectResponse404, GetProjectResponse500]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        width=width,
        height=height,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: int,
    *,
    client: {},
    width: Union[Unset, None, str] = "100%",
    height: Union[Unset, None, str] = "auto",
) -> Optional[Union[GetProjectResponse200, GetProjectResponse401, GetProjectResponse404, GetProjectResponse500]]:
    """Show a certain project.

     View a specific project by project ID.

    Args:
        project_id (int):  Example: 1.
        width (Union[Unset, None, str]):  Default: '100%'. Example: 50rem.
        height (Union[Unset, None, str]):  Default: 'auto'. Example: 50rem.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetProjectResponse200, GetProjectResponse401, GetProjectResponse404, GetProjectResponse500]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            width=width,
            height=height,
        )
    ).parsed
