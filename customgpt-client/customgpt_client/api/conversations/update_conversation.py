import json
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import requests

from ... import errors
from ...models.update_conversation_json_body import UpdateConversationJsonBody
from ...models.update_conversation_response_200 import UpdateConversationResponse200
from ...models.update_conversation_response_400 import UpdateConversationResponse400
from ...models.update_conversation_response_401 import UpdateConversationResponse401
from ...models.update_conversation_response_404 import UpdateConversationResponse404
from ...models.update_conversation_response_500 import UpdateConversationResponse500
from ...types import Response


def _get_kwargs(
    project_id: int,
    session_id: str,
    *,
    client: {},
    json_body: UpdateConversationJsonBody,
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectId}/conversations/{sessionId}".format(
        client.base_url, projectId=project_id, sessionId=session_id
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


def _parse_response(
    *, client: {}, response: None
) -> Optional[
    Union[
        UpdateConversationResponse200,
        UpdateConversationResponse400,
        UpdateConversationResponse401,
        UpdateConversationResponse404,
        UpdateConversationResponse500,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UpdateConversationResponse200.from_dict(json.loads(response.text))

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = UpdateConversationResponse400.from_dict(json.loads(response.text))

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = UpdateConversationResponse401.from_dict(json.loads(response.text))

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = UpdateConversationResponse404.from_dict(json.loads(response.text))

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = UpdateConversationResponse500.from_dict(json.loads(response.text))

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: {}, response: None, content: Optional[bytes] = None
) -> Response[
    Union[
        UpdateConversationResponse200,
        UpdateConversationResponse400,
        UpdateConversationResponse401,
        UpdateConversationResponse404,
        UpdateConversationResponse500,
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
    session_id: str,
    *,
    client: {},
    json_body: UpdateConversationJsonBody,
):
    """Update a conversation.

     Update a conversation within a project identified by its unique projectId and sessionId. This
    endpoint allows you to modify and update the properties of a specific conversation. By providing the
    projectId and sessionId, you can target the desired conversation and make changes to its attributes.
    Here is an example to update a conversation: [API](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/Update_Delete_a_conversation.ipynb) [SDK](https://github.com/Poll-The-
    People/customgpt-cookbook/blob/main/examples/SDK_Update_Delete_a_conversation.ipynb).

    Args:
        project_id (int):
        session_id (str):
        json_body (UpdateConversationJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[UpdateConversationResponse200, UpdateConversationResponse400, UpdateConversationResponse401, UpdateConversationResponse404, UpdateConversationResponse500]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        session_id=session_id,
        client=client,
        json_body=json_body,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: int,
    session_id: str,
    *,
    client: {},
    json_body: UpdateConversationJsonBody,
) -> Optional[
    Union[
        UpdateConversationResponse200,
        UpdateConversationResponse400,
        UpdateConversationResponse401,
        UpdateConversationResponse404,
        UpdateConversationResponse500,
    ]
]:
    """Update a conversation.

     Update a conversation within a project identified by its unique projectId and sessionId. This
    endpoint allows you to modify and update the properties of a specific conversation. By providing the
    projectId and sessionId, you can target the desired conversation and make changes to its attributes.
    Here is an example to update a conversation: [API](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/Update_Delete_a_conversation.ipynb) [SDK](https://github.com/Poll-The-
    People/customgpt-cookbook/blob/main/examples/SDK_Update_Delete_a_conversation.ipynb).

    Args:
        project_id (int):
        session_id (str):
        json_body (UpdateConversationJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[UpdateConversationResponse200, UpdateConversationResponse400, UpdateConversationResponse401, UpdateConversationResponse404, UpdateConversationResponse500]
    """

    return sync_detailed(
        project_id=project_id,
        session_id=session_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    session_id: str,
    *,
    client: {},
    json_body: UpdateConversationJsonBody,
) -> Response[
    Union[
        UpdateConversationResponse200,
        UpdateConversationResponse400,
        UpdateConversationResponse401,
        UpdateConversationResponse404,
        UpdateConversationResponse500,
    ]
]:
    kwargs = _get_kwargs(
        project_id=project_id,
        session_id=session_id,
        client=client,
        json_body=json_body,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: int,
    session_id: str,
    *,
    client: {},
    json_body: UpdateConversationJsonBody,
) -> Optional[
    Union[
        UpdateConversationResponse200,
        UpdateConversationResponse400,
        UpdateConversationResponse401,
        UpdateConversationResponse404,
        UpdateConversationResponse500,
    ]
]:
    """Update a conversation.

     Update a conversation within a project identified by its unique projectId and sessionId. This
    endpoint allows you to modify and update the properties of a specific conversation. By providing the
    projectId and sessionId, you can target the desired conversation and make changes to its attributes.
    Here is an example to update a conversation: [API](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/Update_Delete_a_conversation.ipynb) [SDK](https://github.com/Poll-The-
    People/customgpt-cookbook/blob/main/examples/SDK_Update_Delete_a_conversation.ipynb).

    Args:
        project_id (int):
        session_id (str):
        json_body (UpdateConversationJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[UpdateConversationResponse200, UpdateConversationResponse400, UpdateConversationResponse401, UpdateConversationResponse404, UpdateConversationResponse500]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            session_id=session_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
