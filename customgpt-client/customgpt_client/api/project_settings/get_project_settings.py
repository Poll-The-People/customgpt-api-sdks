import json
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import requests

from ... import errors
from ...models.get_project_settings_response_200 import GetProjectSettingsResponse200
from ...models.get_project_settings_response_400 import GetProjectSettingsResponse400
from ...models.get_project_settings_response_401 import GetProjectSettingsResponse401
from ...models.get_project_settings_response_404 import GetProjectSettingsResponse404
from ...models.get_project_settings_response_500 import GetProjectSettingsResponse500
from ...types import Response


def _get_kwargs(
    project_id: int,
    *,
    client: {},
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectId}/settings".format(client.base_url, projectId=project_id)

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


def _parse_response(*, client: {}, response: None) -> Optional[
    Union[
        GetProjectSettingsResponse200,
        GetProjectSettingsResponse400,
        GetProjectSettingsResponse401,
        GetProjectSettingsResponse404,
        GetProjectSettingsResponse500,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetProjectSettingsResponse200.from_dict(json.loads(response.text))

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetProjectSettingsResponse400.from_dict(json.loads(response.text))

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetProjectSettingsResponse401.from_dict(json.loads(response.text))

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetProjectSettingsResponse404.from_dict(json.loads(response.text))

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetProjectSettingsResponse500.from_dict(json.loads(response.text))

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: {}, response: None, content: Optional[bytes] = None) -> Response[
    Union[
        GetProjectSettingsResponse200,
        GetProjectSettingsResponse400,
        GetProjectSettingsResponse401,
        GetProjectSettingsResponse404,
        GetProjectSettingsResponse500,
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
):
    """Get project settings.

     Retrieve the project settings for a specific project. This endpoint allows you to fetch the
    configuration and settings associated with the project.
    Here is an example to get a project settings: [API](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/Get_Settings_for_a_particular_project.ipynb)
    [SDK](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/SDK_Get_settings_for_a_particular_project.ipynb).

    Args:
        project_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetProjectSettingsResponse200, GetProjectSettingsResponse400, GetProjectSettingsResponse401, GetProjectSettingsResponse404, GetProjectSettingsResponse500]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: int,
    *,
    client: {},
) -> Optional[
    Union[
        GetProjectSettingsResponse200,
        GetProjectSettingsResponse400,
        GetProjectSettingsResponse401,
        GetProjectSettingsResponse404,
        GetProjectSettingsResponse500,
    ]
]:
    """Get project settings.

     Retrieve the project settings for a specific project. This endpoint allows you to fetch the
    configuration and settings associated with the project.
    Here is an example to get a project settings: [API](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/Get_Settings_for_a_particular_project.ipynb)
    [SDK](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/SDK_Get_settings_for_a_particular_project.ipynb).

    Args:
        project_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetProjectSettingsResponse200, GetProjectSettingsResponse400, GetProjectSettingsResponse401, GetProjectSettingsResponse404, GetProjectSettingsResponse500]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    *,
    client: {},
) -> Response[
    Union[
        GetProjectSettingsResponse200,
        GetProjectSettingsResponse400,
        GetProjectSettingsResponse401,
        GetProjectSettingsResponse404,
        GetProjectSettingsResponse500,
    ]
]:

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: int,
    *,
    client: {},
) -> Optional[
    Union[
        GetProjectSettingsResponse200,
        GetProjectSettingsResponse400,
        GetProjectSettingsResponse401,
        GetProjectSettingsResponse404,
        GetProjectSettingsResponse500,
    ]
]:
    """Get project settings.

     Retrieve the project settings for a specific project. This endpoint allows you to fetch the
    configuration and settings associated with the project.
    Here is an example to get a project settings: [API](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/Get_Settings_for_a_particular_project.ipynb)
    [SDK](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/SDK_Get_settings_for_a_particular_project.ipynb).

    Args:
        project_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetProjectSettingsResponse200, GetProjectSettingsResponse400, GetProjectSettingsResponse401, GetProjectSettingsResponse404, GetProjectSettingsResponse500]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
        )
    ).parsed
