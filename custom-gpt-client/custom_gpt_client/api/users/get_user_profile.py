from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import CustomGPT, CustomGPTClient
from ...models.get_user_profile_response_200 import GetUserProfileResponse200
from ...types import Response


def _get_kwargs(
    *,
    client: CustomGPT,
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
    *, client: CustomGPTClient, response: httpx.Response
) -> Optional[Union[Any, GetUserProfileResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetUserProfileResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: CustomGPTClient, response: httpx.Response
) -> Response[Union[Any, GetUserProfileResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: CustomGPT,
) -> Response[Union[Any, GetUserProfileResponse200]]:
    """Show the user's profile.

     Retrieve the current user's profile.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetUserProfileResponse200]]
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
    client: CustomGPT,
) -> Optional[Union[Any, GetUserProfileResponse200]]:
    """Show the user's profile.

     Retrieve the current user's profile.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetUserProfileResponse200]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: CustomGPT,
) -> Response[Union[Any, GetUserProfileResponse200]]:
    """Show the user's profile.

     Retrieve the current user's profile.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetUserProfileResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: CustomGPT,
) -> Optional[Union[Any, GetUserProfileResponse200]]:
    """Show the user's profile.

     Retrieve the current user's profile.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetUserProfileResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
