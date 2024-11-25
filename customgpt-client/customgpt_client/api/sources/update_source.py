import json
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import requests

from ... import errors
from ...models.update_source_json_body import UpdateSourceJsonBody
from ...models.update_source_response_201 import UpdateSourceResponse201
from ...models.update_source_response_400 import UpdateSourceResponse400
from ...models.update_source_response_401 import UpdateSourceResponse401
from ...models.update_source_response_404 import UpdateSourceResponse404
from ...models.update_source_response_500 import UpdateSourceResponse500
from ...types import Response


def _get_kwargs(
    project_id: int,
    source_id: int,
    *,
    client: {},
    json_body: UpdateSourceJsonBody,
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectId}/sources/{sourceId}".format(
        client.base_url, projectId=project_id, sourceId=source_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "allow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: {}, response: None) -> Optional[
    Union[
        UpdateSourceResponse201,
        UpdateSourceResponse400,
        UpdateSourceResponse401,
        UpdateSourceResponse404,
        UpdateSourceResponse500,
    ]
]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = UpdateSourceResponse201.from_dict(json.loads(response.text))

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = UpdateSourceResponse400.from_dict(json.loads(response.text))

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = UpdateSourceResponse401.from_dict(json.loads(response.text))

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = UpdateSourceResponse404.from_dict(json.loads(response.text))

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = UpdateSourceResponse500.from_dict(json.loads(response.text))

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: {}, response: None, content: Optional[bytes] = None) -> Response[
    Union[
        UpdateSourceResponse201,
        UpdateSourceResponse400,
        UpdateSourceResponse401,
        UpdateSourceResponse404,
        UpdateSourceResponse500,
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
    source_id: int,
    *,
    client: {},
    json_body: UpdateSourceJsonBody,
):
    """Update project source settings.

     Update a data source settings, allowing you to change additional settings.

    Args:
        project_id (int):
        source_id (int):
        json_body (UpdateSourceJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[UpdateSourceResponse201, UpdateSourceResponse400, UpdateSourceResponse401, UpdateSourceResponse404, UpdateSourceResponse500]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        source_id=source_id,
        client=client,
        json_body=json_body,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: int,
    source_id: int,
    *,
    client: {},
    json_body: UpdateSourceJsonBody,
) -> Optional[
    Union[
        UpdateSourceResponse201,
        UpdateSourceResponse400,
        UpdateSourceResponse401,
        UpdateSourceResponse404,
        UpdateSourceResponse500,
    ]
]:
    """Update project source settings.

     Update a data source settings, allowing you to change additional settings.

    Args:
        project_id (int):
        source_id (int):
        json_body (UpdateSourceJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[UpdateSourceResponse201, UpdateSourceResponse400, UpdateSourceResponse401, UpdateSourceResponse404, UpdateSourceResponse500]
    """

    return sync_detailed(
        project_id=project_id,
        source_id=source_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    source_id: int,
    *,
    client: {},
    json_body: UpdateSourceJsonBody,
) -> Response[
    Union[
        UpdateSourceResponse201,
        UpdateSourceResponse400,
        UpdateSourceResponse401,
        UpdateSourceResponse404,
        UpdateSourceResponse500,
    ]
]:

    kwargs = _get_kwargs(
        project_id=project_id,
        source_id=source_id,
        client=client,
        json_body=json_body,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: int,
    source_id: int,
    *,
    client: {},
    json_body: UpdateSourceJsonBody,
) -> Optional[
    Union[
        UpdateSourceResponse201,
        UpdateSourceResponse400,
        UpdateSourceResponse401,
        UpdateSourceResponse404,
        UpdateSourceResponse500,
    ]
]:
    """Update project source settings.

     Update a data source settings, allowing you to change additional settings.

    Args:
        project_id (int):
        source_id (int):
        json_body (UpdateSourceJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[UpdateSourceResponse201, UpdateSourceResponse400, UpdateSourceResponse401, UpdateSourceResponse404, UpdateSourceResponse500]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            source_id=source_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
