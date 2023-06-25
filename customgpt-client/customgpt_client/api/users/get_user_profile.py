from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...models.get_user_profile_response_200 import GetUserProfileResponse200
from ...models.get_user_profile_response_401 import GetUserProfileResponse401
from ...models.get_user_profile_response_500 import GetUserProfileResponse500
from ...types import Response


def _get_kwargs(
    *,
    client: {},
) -> Dict[str, Any]:
    url = "{}/api/v1/user".format(client.base_url)

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
) -> Optional[Union[GetUserProfileResponse200, GetUserProfileResponse401, GetUserProfileResponse500]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetUserProfileResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetUserProfileResponse401.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetUserProfileResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: {}, response: httpx.Response, content: Optional[bytes] = None
) -> Response[Union[GetUserProfileResponse200, GetUserProfileResponse401, GetUserProfileResponse500]]:
    parse = _parse_response(client=client, response=response)
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content if content is None else content,
        headers=response.headers,
        parsed=parse,
    )


def sync_detailed(
    *,
    client: {},
):
    """Show the user's profile.

     Retrieve the current user's profile.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetUserProfileResponse200, GetUserProfileResponse401, GetUserProfileResponse500]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: {},
) -> Optional[Union[GetUserProfileResponse200, GetUserProfileResponse401, GetUserProfileResponse500]]:
    """Show the user's profile.

     Retrieve the current user's profile.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetUserProfileResponse200, GetUserProfileResponse401, GetUserProfileResponse500]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: {},
) -> Response[Union[GetUserProfileResponse200, GetUserProfileResponse401, GetUserProfileResponse500]]:
    """Show the user's profile.

     Retrieve the current user's profile.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetUserProfileResponse200, GetUserProfileResponse401, GetUserProfileResponse500]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: {},
) -> Optional[Union[GetUserProfileResponse200, GetUserProfileResponse401, GetUserProfileResponse500]]:
    """Show the user's profile.

     Retrieve the current user's profile.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetUserProfileResponse200, GetUserProfileResponse401, GetUserProfileResponse500]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
