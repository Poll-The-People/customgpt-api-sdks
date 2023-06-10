from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...models.get_open_graph_data_for_citation_response_200 import GetOpenGraphDataForCitationResponse200
from ...types import Response


def _get_kwargs(
    project_id: int,
    citation_id: int,
    *,
    client: {},
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectId}/citations/{citationId}".format(
        client.base_url, projectId=project_id, citationId=citation_id
    )

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
) -> Optional[Union[Any, GetOpenGraphDataForCitationResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetOpenGraphDataForCitationResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: {}, response: httpx.Response
) -> Response[Union[Any, GetOpenGraphDataForCitationResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: int,
    citation_id: int,
    *,
    client: {},
) -> Response[Union[Any, GetOpenGraphDataForCitationResponse200]]:
    """Get the Open Graph data for a citation.

     Get the Open Graph data for a citation by its unique identifier.

    Args:
        project_id (int):
        citation_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetOpenGraphDataForCitationResponse200]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        citation_id=citation_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)