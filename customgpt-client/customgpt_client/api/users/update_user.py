import json
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import requests

from ... import errors
from ...models.update_user_multipart_data import UpdateUserMultipartData
from ...models.update_user_response_200 import UpdateUserResponse200
from ...models.update_user_response_401 import UpdateUserResponse401
from ...models.update_user_response_500 import UpdateUserResponse500
from ...types import Response


def _get_kwargs(
    *,
    client: {},
    multipart_data: UpdateUserMultipartData,
) -> Dict[str, Any]:
    url = "{}/api/v1/user".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "allow_redirects": client.follow_redirects,
        "files": multipart_multipart_data,
    }


def _parse_response(
    *, client: {}, response: None
) -> Optional[Union[UpdateUserResponse200, UpdateUserResponse401, UpdateUserResponse500]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UpdateUserResponse200.from_dict(json.loads(response.text))

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = UpdateUserResponse401.from_dict(json.loads(response.text))

        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = UpdateUserResponse500.from_dict(json.loads(response.text))

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: {}, response: None, content: Optional[bytes] = None
) -> Response[Union[UpdateUserResponse200, UpdateUserResponse401, UpdateUserResponse500]]:
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
    multipart_data: UpdateUserMultipartData,
):
    """Update the user's profile.

     Update the profile of the current user. This endpoint allows the user to modify and update their
    profile information and preferences within the application or system.

    Args:
        multipart_data (UpdateUserMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[UpdateUserResponse200, UpdateUserResponse401, UpdateUserResponse500]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: {},
    multipart_data: UpdateUserMultipartData,
) -> Optional[Union[UpdateUserResponse200, UpdateUserResponse401, UpdateUserResponse500]]:
    """Update the user's profile.

     Update the profile of the current user. This endpoint allows the user to modify and update their
    profile information and preferences within the application or system.

    Args:
        multipart_data (UpdateUserMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[UpdateUserResponse200, UpdateUserResponse401, UpdateUserResponse500]
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: {},
    multipart_data: UpdateUserMultipartData,
) -> Response[Union[UpdateUserResponse200, UpdateUserResponse401, UpdateUserResponse500]]:
    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: {},
    multipart_data: UpdateUserMultipartData,
) -> Optional[Union[UpdateUserResponse200, UpdateUserResponse401, UpdateUserResponse500]]:
    """Update the user's profile.

     Update the profile of the current user. This endpoint allows the user to modify and update their
    profile information and preferences within the application or system.

    Args:
        multipart_data (UpdateUserMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[UpdateUserResponse200, UpdateUserResponse401, UpdateUserResponse500]
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
