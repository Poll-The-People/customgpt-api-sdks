import json
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import requests

from ... import errors
from ...models.traffic_reports_filters_item import TrafficReportsFiltersItem
from ...models.traffic_reports_response_200 import TrafficReportsResponse200
from ...models.traffic_reports_response_400 import TrafficReportsResponse400
from ...models.traffic_reports_response_401 import TrafficReportsResponse401
from ...models.traffic_reports_response_404 import TrafficReportsResponse404
from ...models.traffic_reports_response_500 import TrafficReportsResponse500
from ...types import UNSET, Response


def _get_kwargs(
    project_id: int,
    *,
    client: {},
    filters: List[TrafficReportsFiltersItem],
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectId}/reports/traffic".format(client.base_url, projectId=project_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_filters = []
    for filters_item_data in filters:
        filters_item = filters_item_data

        json_filters.append(filters_item)

    params["filters"] = json_filters

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


def _parse_response(*, client: {}, response: None) -> Optional[
    Union[
        TrafficReportsResponse200,
        TrafficReportsResponse400,
        TrafficReportsResponse401,
        TrafficReportsResponse404,
        TrafficReportsResponse500,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TrafficReportsResponse200.from_dict(json.loads(response.text))

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = TrafficReportsResponse400.from_dict(json.loads(response.text))

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = TrafficReportsResponse401.from_dict(json.loads(response.text))

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = TrafficReportsResponse404.from_dict(json.loads(response.text))

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = TrafficReportsResponse500.from_dict(json.loads(response.text))

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: {}, response: None, content: Optional[bytes] = None) -> Response[
    Union[
        TrafficReportsResponse200,
        TrafficReportsResponse400,
        TrafficReportsResponse401,
        TrafficReportsResponse404,
        TrafficReportsResponse500,
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
    filters: List[TrafficReportsFiltersItem],
):
    """Provide summary of various metrics of users interactions with the application.

     Provide summary of various metrics of users interactions with the application such as the users
    number (both named and anonymous),
    their geographical locations, the browsers they use, and the sources from which they arrived at the
    application.

    Args:
        project_id (int):  Example: 1.
        filters (List[TrafficReportsFiltersItem]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[TrafficReportsResponse200, TrafficReportsResponse400, TrafficReportsResponse401, TrafficReportsResponse404, TrafficReportsResponse500]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        filters=filters,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: int,
    *,
    client: {},
    filters: List[TrafficReportsFiltersItem],
) -> Optional[
    Union[
        TrafficReportsResponse200,
        TrafficReportsResponse400,
        TrafficReportsResponse401,
        TrafficReportsResponse404,
        TrafficReportsResponse500,
    ]
]:
    """Provide summary of various metrics of users interactions with the application.

     Provide summary of various metrics of users interactions with the application such as the users
    number (both named and anonymous),
    their geographical locations, the browsers they use, and the sources from which they arrived at the
    application.

    Args:
        project_id (int):  Example: 1.
        filters (List[TrafficReportsFiltersItem]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[TrafficReportsResponse200, TrafficReportsResponse400, TrafficReportsResponse401, TrafficReportsResponse404, TrafficReportsResponse500]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        filters=filters,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    *,
    client: {},
    filters: List[TrafficReportsFiltersItem],
) -> Response[
    Union[
        TrafficReportsResponse200,
        TrafficReportsResponse400,
        TrafficReportsResponse401,
        TrafficReportsResponse404,
        TrafficReportsResponse500,
    ]
]:

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        filters=filters,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: int,
    *,
    client: {},
    filters: List[TrafficReportsFiltersItem],
) -> Optional[
    Union[
        TrafficReportsResponse200,
        TrafficReportsResponse400,
        TrafficReportsResponse401,
        TrafficReportsResponse404,
        TrafficReportsResponse500,
    ]
]:
    """Provide summary of various metrics of users interactions with the application.

     Provide summary of various metrics of users interactions with the application such as the users
    number (both named and anonymous),
    their geographical locations, the browsers they use, and the sources from which they arrived at the
    application.

    Args:
        project_id (int):  Example: 1.
        filters (List[TrafficReportsFiltersItem]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[TrafficReportsResponse200, TrafficReportsResponse400, TrafficReportsResponse401, TrafficReportsResponse404, TrafficReportsResponse500]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            filters=filters,
        )
    ).parsed
