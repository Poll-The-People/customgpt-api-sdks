from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...models.update_user_profile_multipart_data import UpdateUserProfileMultipartData
from ...models.update_user_profile_response_200 import UpdateUserProfileResponse200
from ...types import Response


def _get_kwargs(
    *,
    client: {},
    multipart_data: UpdateUserProfileMultipartData,
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
        "follow_redirects": client.follow_redirects,
        "files": multipart_multipart_data,
    }


def _parse_response(*, client: {}, response: httpx.Response) -> Optional[Union[Any, UpdateUserProfileResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UpdateUserProfileResponse200.from_dict(response.json())

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


def _build_response(*, client: {}, response: httpx.Response) -> Response[Union[Any, UpdateUserProfileResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: {},
    multipart_data: UpdateUserProfileMultipartData,
) -> Response[Union[Any, UpdateUserProfileResponse200]]:
    """Update the user's profile.

     Update the current user's profile.

    Args:
        multipart_data (UpdateUserProfileMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateUserProfileResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)