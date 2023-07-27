import json
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import requests

from ... import errors
from ...models.get_citation_response_200 import GetCitationResponse200
from ...models.get_citation_response_400 import GetCitationResponse400
from ...models.get_citation_response_401 import GetCitationResponse401
from ...models.get_citation_response_404 import GetCitationResponse404
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
        "allow_redirects": client.follow_redirects,
    }


def _parse_response(
    *, client: {}, response: None
) -> Optional[Union[GetCitationResponse200, GetCitationResponse400, GetCitationResponse401, GetCitationResponse404]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetCitationResponse200.from_dict(json.loads(response.text))

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetCitationResponse400.from_dict(json.loads(response.text))

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetCitationResponse401.from_dict(json.loads(response.text))

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetCitationResponse404.from_dict(json.loads(response.text))

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: {}, response: None, content: Optional[bytes] = None
) -> Response[Union[GetCitationResponse200, GetCitationResponse400, GetCitationResponse401, GetCitationResponse404]]:
    parse = _parse_response(client=client, response=response)
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content if content is None else content,
        headers=response.headers,
        parsed=parse,
    )


def sync_detailed(
    project_id: int,
    citation_id: int,
    *,
    client: {},
):
    """Get the Open Graph data for a citation.

     Retrieve the Open Graph data for a citation based on its unique identifier. This endpoint allows you
    to fetch the Open Graph metadata associated with a specific citation.
    Here is an example to get citation detail: [API](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/Get_citation_details.ipynb) [SDK](https://github.com/Poll-The-
    People/customgpt-cookbook/blob/main/examples/SDK_Get_Citation_Details.ipynb).

    Args:
        project_id (int):
        citation_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetCitationResponse200, GetCitationResponse400, GetCitationResponse401, GetCitationResponse404]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        citation_id=citation_id,
        client=client,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: int,
    citation_id: int,
    *,
    client: {},
) -> Optional[Union[GetCitationResponse200, GetCitationResponse400, GetCitationResponse401, GetCitationResponse404]]:
    """Get the Open Graph data for a citation.

     Retrieve the Open Graph data for a citation based on its unique identifier. This endpoint allows you
    to fetch the Open Graph metadata associated with a specific citation.
    Here is an example to get citation detail: [API](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/Get_citation_details.ipynb) [SDK](https://github.com/Poll-The-
    People/customgpt-cookbook/blob/main/examples/SDK_Get_Citation_Details.ipynb).

    Args:
        project_id (int):
        citation_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetCitationResponse200, GetCitationResponse400, GetCitationResponse401, GetCitationResponse404]
    """

    return sync_detailed(
        project_id=project_id,
        citation_id=citation_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    citation_id: int,
    *,
    client: {},
) -> Response[Union[GetCitationResponse200, GetCitationResponse400, GetCitationResponse401, GetCitationResponse404]]:
    kwargs = _get_kwargs(
        project_id=project_id,
        citation_id=citation_id,
        client=client,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: int,
    citation_id: int,
    *,
    client: {},
) -> Optional[Union[GetCitationResponse200, GetCitationResponse400, GetCitationResponse401, GetCitationResponse404]]:
    """Get the Open Graph data for a citation.

     Retrieve the Open Graph data for a citation based on its unique identifier. This endpoint allows you
    to fetch the Open Graph metadata associated with a specific citation.
    Here is an example to get citation detail: [API](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/Get_citation_details.ipynb) [SDK](https://github.com/Poll-The-
    People/customgpt-cookbook/blob/main/examples/SDK_Get_Citation_Details.ipynb).

    Args:
        project_id (int):
        citation_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetCitationResponse200, GetCitationResponse400, GetCitationResponse401, GetCitationResponse404]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            citation_id=citation_id,
            client=client,
        )
    ).parsed
