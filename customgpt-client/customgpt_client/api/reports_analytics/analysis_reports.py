import json
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import requests

from ... import errors
from ...models.analysis_reports_filters_item import AnalysisReportsFiltersItem
from ...models.analysis_reports_interval import AnalysisReportsInterval
from ...models.analysis_reports_response_200 import AnalysisReportsResponse200
from ...models.analysis_reports_response_400 import AnalysisReportsResponse400
from ...models.analysis_reports_response_401 import AnalysisReportsResponse401
from ...models.analysis_reports_response_404 import AnalysisReportsResponse404
from ...models.analysis_reports_response_500 import AnalysisReportsResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: int,
    *,
    client: {},
    filters: List[AnalysisReportsFiltersItem],
    interval: Union[Unset, None, AnalysisReportsInterval] = AnalysisReportsInterval.WEEKLY,
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectId}/reports/analysis".format(client.base_url, projectId=project_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_filters = []
    for filters_item_data in filters:
        filters_item = filters_item_data

        json_filters.append(filters_item)

    params["filters"] = json_filters

    json_interval: Union[Unset, None, str] = UNSET
    if not isinstance(interval, Unset):
        json_interval = interval if interval else None

    params["interval"] = json_interval

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
        AnalysisReportsResponse200,
        AnalysisReportsResponse400,
        AnalysisReportsResponse401,
        AnalysisReportsResponse404,
        AnalysisReportsResponse500,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AnalysisReportsResponse200.from_dict(json.loads(response.text))

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = AnalysisReportsResponse400.from_dict(json.loads(response.text))

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = AnalysisReportsResponse401.from_dict(json.loads(response.text))

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = AnalysisReportsResponse404.from_dict(json.loads(response.text))

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = AnalysisReportsResponse500.from_dict(json.loads(response.text))

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: {}, response: None, content: Optional[bytes] = None) -> Response[
    Union[
        AnalysisReportsResponse200,
        AnalysisReportsResponse400,
        AnalysisReportsResponse401,
        AnalysisReportsResponse404,
        AnalysisReportsResponse500,
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
    filters: List[AnalysisReportsFiltersItem],
    interval: Union[Unset, None, AnalysisReportsInterval] = AnalysisReportsInterval.WEEKLY,
):
    """Provide graph-ready analysis data of various metrics.

    Args:
        project_id (int):  Example: 1.
        filters (List[AnalysisReportsFiltersItem]):
        interval (Union[Unset, None, AnalysisReportsInterval]):  Default:
            AnalysisReportsInterval.WEEKLY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AnalysisReportsResponse200, AnalysisReportsResponse400, AnalysisReportsResponse401, AnalysisReportsResponse404, AnalysisReportsResponse500]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        filters=filters,
        interval=interval,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: int,
    *,
    client: {},
    filters: List[AnalysisReportsFiltersItem],
    interval: Union[Unset, None, AnalysisReportsInterval] = AnalysisReportsInterval.WEEKLY,
) -> Optional[
    Union[
        AnalysisReportsResponse200,
        AnalysisReportsResponse400,
        AnalysisReportsResponse401,
        AnalysisReportsResponse404,
        AnalysisReportsResponse500,
    ]
]:
    """Provide graph-ready analysis data of various metrics.

    Args:
        project_id (int):  Example: 1.
        filters (List[AnalysisReportsFiltersItem]):
        interval (Union[Unset, None, AnalysisReportsInterval]):  Default:
            AnalysisReportsInterval.WEEKLY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AnalysisReportsResponse200, AnalysisReportsResponse400, AnalysisReportsResponse401, AnalysisReportsResponse404, AnalysisReportsResponse500]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        filters=filters,
        interval=interval,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    *,
    client: {},
    filters: List[AnalysisReportsFiltersItem],
    interval: Union[Unset, None, AnalysisReportsInterval] = AnalysisReportsInterval.WEEKLY,
) -> Response[
    Union[
        AnalysisReportsResponse200,
        AnalysisReportsResponse400,
        AnalysisReportsResponse401,
        AnalysisReportsResponse404,
        AnalysisReportsResponse500,
    ]
]:

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        filters=filters,
        interval=interval,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: int,
    *,
    client: {},
    filters: List[AnalysisReportsFiltersItem],
    interval: Union[Unset, None, AnalysisReportsInterval] = AnalysisReportsInterval.WEEKLY,
) -> Optional[
    Union[
        AnalysisReportsResponse200,
        AnalysisReportsResponse400,
        AnalysisReportsResponse401,
        AnalysisReportsResponse404,
        AnalysisReportsResponse500,
    ]
]:
    """Provide graph-ready analysis data of various metrics.

    Args:
        project_id (int):  Example: 1.
        filters (List[AnalysisReportsFiltersItem]):
        interval (Union[Unset, None, AnalysisReportsInterval]):  Default:
            AnalysisReportsInterval.WEEKLY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AnalysisReportsResponse200, AnalysisReportsResponse400, AnalysisReportsResponse401, AnalysisReportsResponse404, AnalysisReportsResponse500]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            filters=filters,
            interval=interval,
        )
    ).parsed
