import json
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import requests

from ... import errors
from ...models.get_conversations_order import GetConversationsOrder
from ...models.get_conversations_response_200 import GetConversationsResponse200
from ...models.get_conversations_response_400 import GetConversationsResponse400
from ...models.get_conversations_response_401 import GetConversationsResponse401
from ...models.get_conversations_response_404 import GetConversationsResponse404
from ...models.get_conversations_response_500 import GetConversationsResponse500
from ...models.get_conversations_user_filter import GetConversationsUserFilter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: int,
    *,
    client: {},
    page: Union[Unset, None, int] = 1,
    order: Union[Unset, None, GetConversationsOrder] = GetConversationsOrder.DESC,
    user_filter: Union[Unset, None, GetConversationsUserFilter] = GetConversationsUserFilter.ALL,
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectId}/conversations".format(client.base_url, projectId=project_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    json_order: Union[Unset, None, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value if order else None

    params["order"] = json_order

    json_user_filter: Union[Unset, None, str] = UNSET
    if not isinstance(user_filter, Unset):
        json_user_filter = user_filter.value if user_filter else None

    params["userFilter"] = json_user_filter

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
    Union[
        GetConversationsResponse200,
        GetConversationsResponse400,
        GetConversationsResponse401,
        GetConversationsResponse404,
        GetConversationsResponse500,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetConversationsResponse200.from_dict(json.loads(response.text))

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetConversationsResponse400.from_dict(json.loads(response.text))

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetConversationsResponse401.from_dict(json.loads(response.text))

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetConversationsResponse404.from_dict(json.loads(response.text))

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetConversationsResponse500.from_dict(json.loads(response.text))

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: {}, response: None, content: Optional[bytes] = None
) -> Response[
    Union[
        GetConversationsResponse200,
        GetConversationsResponse400,
        GetConversationsResponse401,
        GetConversationsResponse404,
        GetConversationsResponse500,
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
    order: Union[Unset, None, GetConversationsOrder] = GetConversationsOrder.DESC,
    user_filter: Union[Unset, None, GetConversationsUserFilter] = GetConversationsUserFilter.ALL,
):
    """List all conversations for a project.

     Retrieve all conversations associated with a project based on its unique projectId. This endpoint
    allows you to fetch a collection of conversations related to a specific project.

    Args:
        project_id (int):  Example: 1.
        page (Union[Unset, None, int]):  Default: 1.
        order (Union[Unset, None, GetConversationsOrder]):  Default: GetConversationsOrder.DESC.
            Example: desc.
        user_filter (Union[Unset, None, GetConversationsUserFilter]):  Default:
            GetConversationsUserFilter.ALL. Example: all.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetConversationsResponse200, GetConversationsResponse400, GetConversationsResponse401, GetConversationsResponse404, GetConversationsResponse500]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        page=page,
        order=order,
        user_filter=user_filter,
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
    order: Union[Unset, None, GetConversationsOrder] = GetConversationsOrder.DESC,
    user_filter: Union[Unset, None, GetConversationsUserFilter] = GetConversationsUserFilter.ALL,
) -> Optional[
    Union[
        GetConversationsResponse200,
        GetConversationsResponse400,
        GetConversationsResponse401,
        GetConversationsResponse404,
        GetConversationsResponse500,
    ]
]:
    """List all conversations for a project.

     Retrieve all conversations associated with a project based on its unique projectId. This endpoint
    allows you to fetch a collection of conversations related to a specific project.

    Args:
        project_id (int):  Example: 1.
        page (Union[Unset, None, int]):  Default: 1.
        order (Union[Unset, None, GetConversationsOrder]):  Default: GetConversationsOrder.DESC.
            Example: desc.
        user_filter (Union[Unset, None, GetConversationsUserFilter]):  Default:
            GetConversationsUserFilter.ALL. Example: all.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetConversationsResponse200, GetConversationsResponse400, GetConversationsResponse401, GetConversationsResponse404, GetConversationsResponse500]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        page=page,
        order=order,
        user_filter=user_filter,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    *,
    client: {},
    page: Union[Unset, None, int] = 1,
    order: Union[Unset, None, GetConversationsOrder] = GetConversationsOrder.DESC,
    user_filter: Union[Unset, None, GetConversationsUserFilter] = GetConversationsUserFilter.ALL,
) -> Response[
    Union[
        GetConversationsResponse200,
        GetConversationsResponse400,
        GetConversationsResponse401,
        GetConversationsResponse404,
        GetConversationsResponse500,
    ]
]:
    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        page=page,
        order=order,
        user_filter=user_filter,
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
    order: Union[Unset, None, GetConversationsOrder] = GetConversationsOrder.DESC,
    user_filter: Union[Unset, None, GetConversationsUserFilter] = GetConversationsUserFilter.ALL,
) -> Optional[
    Union[
        GetConversationsResponse200,
        GetConversationsResponse400,
        GetConversationsResponse401,
        GetConversationsResponse404,
        GetConversationsResponse500,
    ]
]:
    """List all conversations for a project.

     Retrieve all conversations associated with a project based on its unique projectId. This endpoint
    allows you to fetch a collection of conversations related to a specific project.

    Args:
        project_id (int):  Example: 1.
        page (Union[Unset, None, int]):  Default: 1.
        order (Union[Unset, None, GetConversationsOrder]):  Default: GetConversationsOrder.DESC.
            Example: desc.
        user_filter (Union[Unset, None, GetConversationsUserFilter]):  Default:
            GetConversationsUserFilter.ALL. Example: all.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetConversationsResponse200, GetConversationsResponse400, GetConversationsResponse401, GetConversationsResponse404, GetConversationsResponse500]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            page=page,
            order=order,
            user_filter=user_filter,
        )
    ).parsed
