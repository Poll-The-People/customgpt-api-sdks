import json
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import requests

from ... import errors
from ...models.replicate_project_response_201 import ReplicateProjectResponse201
from ...models.replicate_project_response_400 import ReplicateProjectResponse400
from ...models.replicate_project_response_401 import ReplicateProjectResponse401
from ...models.replicate_project_response_500 import ReplicateProjectResponse500
from ...types import Response


def _get_kwargs(
    project_id: int,
    *,
    client: {},
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectId}/replicate".format(client.base_url, projectId=project_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "allow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: {}, response: None) -> Optional[
    Union[
        ReplicateProjectResponse201,
        ReplicateProjectResponse400,
        ReplicateProjectResponse401,
        ReplicateProjectResponse500,
    ]
]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = ReplicateProjectResponse201.from_dict(json.loads(response.text))

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ReplicateProjectResponse400.from_dict(json.loads(response.text))

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ReplicateProjectResponse401.from_dict(json.loads(response.text))

        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ReplicateProjectResponse500.from_dict(json.loads(response.text))

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: {}, response: None, content: Optional[bytes] = None) -> Response[
    Union[
        ReplicateProjectResponse201,
        ReplicateProjectResponse400,
        ReplicateProjectResponse401,
        ReplicateProjectResponse500,
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
    """Replicate project by given Project ID.

     Create a copy pf project by replicating project info, settings, sitemap sources and uploaded files.
    This endpoint enables you to initiate the replication of a project by supplying the necessary
    project id value. The system will process the replicated data and generate a new project based on
    the information of existing project.

    Args:
        project_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ReplicateProjectResponse201, ReplicateProjectResponse400, ReplicateProjectResponse401, ReplicateProjectResponse500]]
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
        ReplicateProjectResponse201,
        ReplicateProjectResponse400,
        ReplicateProjectResponse401,
        ReplicateProjectResponse500,
    ]
]:
    """Replicate project by given Project ID.

     Create a copy pf project by replicating project info, settings, sitemap sources and uploaded files.
    This endpoint enables you to initiate the replication of a project by supplying the necessary
    project id value. The system will process the replicated data and generate a new project based on
    the information of existing project.

    Args:
        project_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ReplicateProjectResponse201, ReplicateProjectResponse400, ReplicateProjectResponse401, ReplicateProjectResponse500]
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
        ReplicateProjectResponse201,
        ReplicateProjectResponse400,
        ReplicateProjectResponse401,
        ReplicateProjectResponse500,
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
        ReplicateProjectResponse201,
        ReplicateProjectResponse400,
        ReplicateProjectResponse401,
        ReplicateProjectResponse500,
    ]
]:
    """Replicate project by given Project ID.

     Create a copy pf project by replicating project info, settings, sitemap sources and uploaded files.
    This endpoint enables you to initiate the replication of a project by supplying the necessary
    project id value. The system will process the replicated data and generate a new project based on
    the information of existing project.

    Args:
        project_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ReplicateProjectResponse201, ReplicateProjectResponse400, ReplicateProjectResponse401, ReplicateProjectResponse500]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
        )
    ).parsed
