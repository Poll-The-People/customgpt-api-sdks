from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...models.preview_response_401 import PreviewResponse401
from ...models.preview_response_404 import PreviewResponse404
from ...models.preview_response_500 import PreviewResponse500
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
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(
    *, client: {}, response: httpx.Response
) -> Optional[Union[PreviewResponse401, PreviewResponse404, PreviewResponse500]]:
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = PreviewResponse401.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = PreviewResponse404.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = PreviewResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: {}, response: httpx.Response, content: Optional[bytes] = None
) -> Response[Union[PreviewResponse401, PreviewResponse404, PreviewResponse500]]:
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
        Response[Union[PreviewResponse401, PreviewResponse404, PreviewResponse500]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: {},
) -> Optional[Union[PreviewResponse401, PreviewResponse404, PreviewResponse500]]:
    """Preview file from citation.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PreviewResponse401, PreviewResponse404, PreviewResponse500]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: {},
) -> Response[Union[PreviewResponse401, PreviewResponse404, PreviewResponse500]]:
    """Preview file from citation.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PreviewResponse401, PreviewResponse404, PreviewResponse500]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: {},
) -> Optional[Union[PreviewResponse401, PreviewResponse404, PreviewResponse500]]:
    """Preview file from citation.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PreviewResponse401, PreviewResponse404, PreviewResponse500]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
