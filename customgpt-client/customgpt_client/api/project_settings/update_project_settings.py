from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...models.update_project_settings_multipart_data import UpdateProjectSettingsMultipartData
from ...models.update_project_settings_response_200 import UpdateProjectSettingsResponse200
from ...models.update_project_settings_response_400 import UpdateProjectSettingsResponse400
from ...models.update_project_settings_response_401 import UpdateProjectSettingsResponse401
from ...models.update_project_settings_response_500 import UpdateProjectSettingsResponse500
from ...types import Response


def _get_kwargs(
    project_id: int,
    *,
    client: {},
    multipart_data: UpdateProjectSettingsMultipartData,
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectId}/settings".format(client.base_url, projectId=project_id)

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


def _parse_response(
    *, client: {}, response: httpx.Response
) -> Optional[
    Union[
        UpdateProjectSettingsResponse200,
        UpdateProjectSettingsResponse400,
        UpdateProjectSettingsResponse401,
        UpdateProjectSettingsResponse500,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UpdateProjectSettingsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = UpdateProjectSettingsResponse400.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = UpdateProjectSettingsResponse401.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = UpdateProjectSettingsResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: {}, response: httpx.Response, content: Optional[bytes] = None
) -> Response[
    Union[
        UpdateProjectSettingsResponse200,
        UpdateProjectSettingsResponse400,
        UpdateProjectSettingsResponse401,
        UpdateProjectSettingsResponse500,
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
    multipart_data: UpdateProjectSettingsMultipartData,
):
    """Update project settings.

     Update project settings of a specific project by `projectId`.

    Args:
        project_id (int):
        multipart_data (UpdateProjectSettingsMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[UpdateProjectSettingsResponse200, UpdateProjectSettingsResponse400, UpdateProjectSettingsResponse401, UpdateProjectSettingsResponse500]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        multipart_data=multipart_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: int,
    *,
    client: {},
    multipart_data: UpdateProjectSettingsMultipartData,
) -> Optional[
    Union[
        UpdateProjectSettingsResponse200,
        UpdateProjectSettingsResponse400,
        UpdateProjectSettingsResponse401,
        UpdateProjectSettingsResponse500,
    ]
]:
    """Update project settings.

     Update project settings of a specific project by `projectId`.

    Args:
        project_id (int):
        multipart_data (UpdateProjectSettingsMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[UpdateProjectSettingsResponse200, UpdateProjectSettingsResponse400, UpdateProjectSettingsResponse401, UpdateProjectSettingsResponse500]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    *,
    client: {},
    multipart_data: UpdateProjectSettingsMultipartData,
) -> Response[
    Union[
        UpdateProjectSettingsResponse200,
        UpdateProjectSettingsResponse400,
        UpdateProjectSettingsResponse401,
        UpdateProjectSettingsResponse500,
    ]
]:
    """Update project settings.

     Update project settings of a specific project by `projectId`.

    Args:
        project_id (int):
        multipart_data (UpdateProjectSettingsMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[UpdateProjectSettingsResponse200, UpdateProjectSettingsResponse400, UpdateProjectSettingsResponse401, UpdateProjectSettingsResponse500]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: int,
    *,
    client: {},
    multipart_data: UpdateProjectSettingsMultipartData,
) -> Optional[
    Union[
        UpdateProjectSettingsResponse200,
        UpdateProjectSettingsResponse400,
        UpdateProjectSettingsResponse401,
        UpdateProjectSettingsResponse500,
    ]
]:
    """Update project settings.

     Update project settings of a specific project by `projectId`.

    Args:
        project_id (int):
        multipart_data (UpdateProjectSettingsMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[UpdateProjectSettingsResponse200, UpdateProjectSettingsResponse400, UpdateProjectSettingsResponse401, UpdateProjectSettingsResponse500]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
