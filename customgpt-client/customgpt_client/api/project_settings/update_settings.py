import json
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import requests

from ... import errors
from ...models.update_settings_multipart_data import UpdateSettingsMultipartData
from ...models.update_settings_response_200 import UpdateSettingsResponse200
from ...models.update_settings_response_400 import UpdateSettingsResponse400
from ...models.update_settings_response_401 import UpdateSettingsResponse401
from ...models.update_settings_response_500 import UpdateSettingsResponse500
from ...types import Response


def _get_kwargs(
    project_id: int,
    *,
    client: {},
    multipart_data: UpdateSettingsMultipartData,
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
        "allow_redirects": client.follow_redirects,
        "files": multipart_multipart_data,
    }


def _parse_response(
    *, client: {}, response: None
) -> Optional[
    Union[UpdateSettingsResponse200, UpdateSettingsResponse400, UpdateSettingsResponse401, UpdateSettingsResponse500]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UpdateSettingsResponse200.from_dict(json.loads(response.text))

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = UpdateSettingsResponse400.from_dict(json.loads(response.text))

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = UpdateSettingsResponse401.from_dict(json.loads(response.text))

        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = UpdateSettingsResponse500.from_dict(json.loads(response.text))

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: {}, response: None, content: Optional[bytes] = None
) -> Response[
    Union[UpdateSettingsResponse200, UpdateSettingsResponse400, UpdateSettingsResponse401, UpdateSettingsResponse500]
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
    multipart_data: UpdateSettingsMultipartData,
):
    """Update project settings.

     Update the project settings for a specific project. This endpoint allows you to update the
    configuration and settings associated with the project.
    Here is an example to get a project settings: [API](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/Update_settings_for_a_particular_project.ipynb)
    [SDK](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/SDK_Update_project_settings.ipynb).

    Args:
        project_id (int):
        multipart_data (UpdateSettingsMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[UpdateSettingsResponse200, UpdateSettingsResponse400, UpdateSettingsResponse401, UpdateSettingsResponse500]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        multipart_data=multipart_data,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: int,
    *,
    client: {},
    multipart_data: UpdateSettingsMultipartData,
) -> Optional[
    Union[UpdateSettingsResponse200, UpdateSettingsResponse400, UpdateSettingsResponse401, UpdateSettingsResponse500]
]:
    """Update project settings.

     Update the project settings for a specific project. This endpoint allows you to update the
    configuration and settings associated with the project.
    Here is an example to get a project settings: [API](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/Update_settings_for_a_particular_project.ipynb)
    [SDK](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/SDK_Update_project_settings.ipynb).

    Args:
        project_id (int):
        multipart_data (UpdateSettingsMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[UpdateSettingsResponse200, UpdateSettingsResponse400, UpdateSettingsResponse401, UpdateSettingsResponse500]
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
    multipart_data: UpdateSettingsMultipartData,
) -> Response[
    Union[UpdateSettingsResponse200, UpdateSettingsResponse400, UpdateSettingsResponse401, UpdateSettingsResponse500]
]:
    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        multipart_data=multipart_data,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: int,
    *,
    client: {},
    multipart_data: UpdateSettingsMultipartData,
) -> Optional[
    Union[UpdateSettingsResponse200, UpdateSettingsResponse400, UpdateSettingsResponse401, UpdateSettingsResponse500]
]:
    """Update project settings.

     Update the project settings for a specific project. This endpoint allows you to update the
    configuration and settings associated with the project.
    Here is an example to get a project settings: [API](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/Update_settings_for_a_particular_project.ipynb)
    [SDK](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/SDK_Update_project_settings.ipynb).

    Args:
        project_id (int):
        multipart_data (UpdateSettingsMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[UpdateSettingsResponse200, UpdateSettingsResponse400, UpdateSettingsResponse401, UpdateSettingsResponse500]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
