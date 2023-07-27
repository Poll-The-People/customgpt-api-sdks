import json
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import requests

from ... import errors
from ...models.preview_citation_response_400 import PreviewCitationResponse400
from ...models.preview_citation_response_401 import PreviewCitationResponse401
from ...models.preview_citation_response_404 import PreviewCitationResponse404
from ...models.preview_citation_response_500 import PreviewCitationResponse500
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: {},
) -> Dict[str, Any]:
    url = "{}/api/v1/preview/{id}".format(client.base_url, id=id)

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
) -> Optional[
    Union[
        PreviewCitationResponse400, PreviewCitationResponse401, PreviewCitationResponse404, PreviewCitationResponse500
    ]
]:
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = PreviewCitationResponse400.from_dict(json.loads(response.text))

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = PreviewCitationResponse401.from_dict(json.loads(response.text))

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = PreviewCitationResponse404.from_dict(json.loads(response.text))

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = PreviewCitationResponse500.from_dict(json.loads(response.text))

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: {}, response: None, content: Optional[bytes] = None
) -> Response[
    Union[
        PreviewCitationResponse400, PreviewCitationResponse401, PreviewCitationResponse404, PreviewCitationResponse500
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
    id: str,
    *,
    client: {},
):
    """Preview file from citation.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PreviewCitationResponse400, PreviewCitationResponse401, PreviewCitationResponse404, PreviewCitationResponse500]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: {},
) -> Optional[
    Union[
        PreviewCitationResponse400, PreviewCitationResponse401, PreviewCitationResponse404, PreviewCitationResponse500
    ]
]:
    """Preview file from citation.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PreviewCitationResponse400, PreviewCitationResponse401, PreviewCitationResponse404, PreviewCitationResponse500]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: {},
) -> Response[
    Union[
        PreviewCitationResponse400, PreviewCitationResponse401, PreviewCitationResponse404, PreviewCitationResponse500
    ]
]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: {},
) -> Optional[
    Union[
        PreviewCitationResponse400, PreviewCitationResponse401, PreviewCitationResponse404, PreviewCitationResponse500
    ]
]:
    """Preview file from citation.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PreviewCitationResponse400, PreviewCitationResponse401, PreviewCitationResponse404, PreviewCitationResponse500]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
