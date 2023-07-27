import json
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import requests

from ... import errors
from ...models.get_user_response_200 import GetUserResponse200
from ...models.get_user_response_401 import GetUserResponse401
from ...models.get_user_response_500 import GetUserResponse500
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
        "allow_redirects": client.follow_redirects,
    }


def _parse_response(
    *, client: {}, response: None
) -> Optional[Union[GetUserResponse200, GetUserResponse401, GetUserResponse500]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetUserResponse200.from_dict(json.loads(response.text))

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetUserResponse401.from_dict(json.loads(response.text))

        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetUserResponse500.from_dict(json.loads(response.text))

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: {}, response: None, content: Optional[bytes] = None
) -> Response[Union[GetUserResponse200, GetUserResponse401, GetUserResponse500]]:
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

     Retrieve the profile information of the current user. This endpoint allows you to fetch the details
    and attributes associated with the user's profile, providing valuable information about the user's
    account and preferences.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetUserResponse200, GetUserResponse401, GetUserResponse500]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: {},
) -> Optional[Union[GetUserResponse200, GetUserResponse401, GetUserResponse500]]:
    """Show the user's profile.

     Retrieve the profile information of the current user. This endpoint allows you to fetch the details
    and attributes associated with the user's profile, providing valuable information about the user's
    account and preferences.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetUserResponse200, GetUserResponse401, GetUserResponse500]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: {},
) -> Response[Union[GetUserResponse200, GetUserResponse401, GetUserResponse500]]:
    kwargs = _get_kwargs(
        client=client,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: {},
) -> Optional[Union[GetUserResponse200, GetUserResponse401, GetUserResponse500]]:
    """Show the user's profile.

     Retrieve the profile information of the current user. This endpoint allows you to fetch the details
    and attributes associated with the user's profile, providing valuable information about the user's
    account and preferences.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetUserResponse200, GetUserResponse401, GetUserResponse500]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
