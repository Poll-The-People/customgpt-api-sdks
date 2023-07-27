import json
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import requests

from ... import errors
from ...models.get_pages_order import GetPagesOrder
from ...models.get_pages_response_200 import GetPagesResponse200
from ...models.get_pages_response_400 import GetPagesResponse400
from ...models.get_pages_response_401 import GetPagesResponse401
from ...models.get_pages_response_404 import GetPagesResponse404
from ...models.get_pages_response_500 import GetPagesResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: int,
    *,
    client: {},
    page: Union[Unset, None, int] = 1,
    duration: Union[Unset, None, int] = 90,
    order: Union[Unset, None, GetPagesOrder] = GetPagesOrder.DESC,
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
        "allow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(
    *, client: {}, response: None
) -> Optional[
    Union[GetPagesResponse200, GetPagesResponse400, GetPagesResponse401, GetPagesResponse404, GetPagesResponse500]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetPagesResponse200.from_dict(json.loads(response.text))

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetPagesResponse400.from_dict(json.loads(response.text))

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetPagesResponse401.from_dict(json.loads(response.text))

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetPagesResponse404.from_dict(json.loads(response.text))

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetPagesResponse500.from_dict(json.loads(response.text))

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: {}, response: None, content: Optional[bytes] = None
) -> Response[
    Union[GetPagesResponse200, GetPagesResponse400, GetPagesResponse401, GetPagesResponse404, GetPagesResponse500]
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
    order: Union[Unset, None, GetPagesOrder] = GetPagesOrder.DESC,
):
    """List all pages that belong to a project.

     Retrieve a list of all pages associated with a project. This endpoint allows you to fetch project
    details and a collection of pages that belong to a specific project. Each page object includes
    information such as the page ID, URL, hash of the URL, project ID, crawl status, index status, file
    details (if applicable), creation and update timestamps, and other relevant attributes.
    Here is an example to list all pages belonging to project: [API](https://github.com/Poll-The-
    People/customgpt-cookbook/blob/main/examples/List_all_pages_of_a_project.ipynb)
    [SDK](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/SDK_List_all_pages_belonging_to_a_project.ipynb).

    Args:
        project_id (int):  Example: 1.
        page (Union[Unset, None, int]):  Default: 1.
        duration (Union[Unset, None, int]):  Default: 90.
        order (Union[Unset, None, GetPagesOrder]):  Default: GetPagesOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetPagesResponse200, GetPagesResponse400, GetPagesResponse401, GetPagesResponse404, GetPagesResponse500]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        page=page,
        duration=duration,
        order=order,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: int,
    *,
    client: {},
    page: Union[Unset, None, int] = 1,
    duration: Union[Unset, None, int] = 90,
    order: Union[Unset, None, GetPagesOrder] = GetPagesOrder.DESC,
) -> Optional[
    Union[GetPagesResponse200, GetPagesResponse400, GetPagesResponse401, GetPagesResponse404, GetPagesResponse500]
]:
    """List all pages that belong to a project.

     Retrieve a list of all pages associated with a project. This endpoint allows you to fetch project
    details and a collection of pages that belong to a specific project. Each page object includes
    information such as the page ID, URL, hash of the URL, project ID, crawl status, index status, file
    details (if applicable), creation and update timestamps, and other relevant attributes.
    Here is an example to list all pages belonging to project: [API](https://github.com/Poll-The-
    People/customgpt-cookbook/blob/main/examples/List_all_pages_of_a_project.ipynb)
    [SDK](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/SDK_List_all_pages_belonging_to_a_project.ipynb).

    Args:
        project_id (int):  Example: 1.
        page (Union[Unset, None, int]):  Default: 1.
        duration (Union[Unset, None, int]):  Default: 90.
        order (Union[Unset, None, GetPagesOrder]):  Default: GetPagesOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetPagesResponse200, GetPagesResponse400, GetPagesResponse401, GetPagesResponse404, GetPagesResponse500]
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
    order: Union[Unset, None, GetPagesOrder] = GetPagesOrder.DESC,
) -> Response[
    Union[GetPagesResponse200, GetPagesResponse400, GetPagesResponse401, GetPagesResponse404, GetPagesResponse500]
]:
    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        page=page,
        duration=duration,
        order=order,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: int,
    *,
    client: {},
    page: Union[Unset, None, int] = 1,
    duration: Union[Unset, None, int] = 90,
    order: Union[Unset, None, GetPagesOrder] = GetPagesOrder.DESC,
) -> Optional[
    Union[GetPagesResponse200, GetPagesResponse400, GetPagesResponse401, GetPagesResponse404, GetPagesResponse500]
]:
    """List all pages that belong to a project.

     Retrieve a list of all pages associated with a project. This endpoint allows you to fetch project
    details and a collection of pages that belong to a specific project. Each page object includes
    information such as the page ID, URL, hash of the URL, project ID, crawl status, index status, file
    details (if applicable), creation and update timestamps, and other relevant attributes.
    Here is an example to list all pages belonging to project: [API](https://github.com/Poll-The-
    People/customgpt-cookbook/blob/main/examples/List_all_pages_of_a_project.ipynb)
    [SDK](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/SDK_List_all_pages_belonging_to_a_project.ipynb).

    Args:
        project_id (int):  Example: 1.
        page (Union[Unset, None, int]):  Default: 1.
        duration (Union[Unset, None, int]):  Default: 90.
        order (Union[Unset, None, GetPagesOrder]):  Default: GetPagesOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetPagesResponse200, GetPagesResponse400, GetPagesResponse401, GetPagesResponse404, GetPagesResponse500]
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
