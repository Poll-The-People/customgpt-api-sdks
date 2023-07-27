import json
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import requests

from ... import errors
from ...models.create_conversation_json_body import CreateConversationJsonBody
from ...models.create_conversation_response_201 import CreateConversationResponse201
from ...models.create_conversation_response_400 import CreateConversationResponse400
from ...models.create_conversation_response_401 import CreateConversationResponse401
from ...models.create_conversation_response_404 import CreateConversationResponse404
from ...models.create_conversation_response_500 import CreateConversationResponse500
from ...types import Response


def _get_kwargs(
    project_id: int,
    *,
    client: {},
    json_body: CreateConversationJsonBody,
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectId}/conversations".format(client.base_url, projectId=project_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
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
        CreateConversationResponse201,
        CreateConversationResponse400,
        CreateConversationResponse401,
        CreateConversationResponse404,
        CreateConversationResponse500,
    ]
]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CreateConversationResponse201.from_dict(json.loads(response.text))

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = CreateConversationResponse400.from_dict(json.loads(response.text))

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = CreateConversationResponse401.from_dict(json.loads(response.text))

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = CreateConversationResponse404.from_dict(json.loads(response.text))

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = CreateConversationResponse500.from_dict(json.loads(response.text))

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: {}, response: None, content: Optional[bytes] = None
) -> Response[
    Union[
        CreateConversationResponse201,
        CreateConversationResponse400,
        CreateConversationResponse401,
        CreateConversationResponse404,
        CreateConversationResponse500,
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
    json_body: CreateConversationJsonBody,
):
    """Create a new conversation.

     Create a new conversation for a project identified by its unique projectId. This endpoint allows you
    to initiate a new conversation within a specific project. A conversation serves as a platform for
    users to exchange messages regarding project-related matters. By providing the projectId, you can
    establish a conversation within the context of the project allowing you to seamlessly communicate
    with it.
    Here is an example to create a conversation: [API](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/Create_a_new_conversation_and_send_a_message_to_the_conversation.ipynb)
    [SDK](https://github.com/Poll-The-People/customgpt-cookbook/blob/main/examples/SDK_Create_a_new_conv
    ersation_and_send_a_message_to_the_conversation.ipynb).

    Args:
        project_id (int):
        json_body (CreateConversationJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateConversationResponse201, CreateConversationResponse400, CreateConversationResponse401, CreateConversationResponse404, CreateConversationResponse500]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        json_body=json_body,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: int,
    *,
    client: {},
    json_body: CreateConversationJsonBody,
) -> Optional[
    Union[
        CreateConversationResponse201,
        CreateConversationResponse400,
        CreateConversationResponse401,
        CreateConversationResponse404,
        CreateConversationResponse500,
    ]
]:
    """Create a new conversation.

     Create a new conversation for a project identified by its unique projectId. This endpoint allows you
    to initiate a new conversation within a specific project. A conversation serves as a platform for
    users to exchange messages regarding project-related matters. By providing the projectId, you can
    establish a conversation within the context of the project allowing you to seamlessly communicate
    with it.
    Here is an example to create a conversation: [API](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/Create_a_new_conversation_and_send_a_message_to_the_conversation.ipynb)
    [SDK](https://github.com/Poll-The-People/customgpt-cookbook/blob/main/examples/SDK_Create_a_new_conv
    ersation_and_send_a_message_to_the_conversation.ipynb).

    Args:
        project_id (int):
        json_body (CreateConversationJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateConversationResponse201, CreateConversationResponse400, CreateConversationResponse401, CreateConversationResponse404, CreateConversationResponse500]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    *,
    client: {},
    json_body: CreateConversationJsonBody,
) -> Response[
    Union[
        CreateConversationResponse201,
        CreateConversationResponse400,
        CreateConversationResponse401,
        CreateConversationResponse404,
        CreateConversationResponse500,
    ]
]:
    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        json_body=json_body,
    )

    response = requests.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: int,
    *,
    client: {},
    json_body: CreateConversationJsonBody,
) -> Optional[
    Union[
        CreateConversationResponse201,
        CreateConversationResponse400,
        CreateConversationResponse401,
        CreateConversationResponse404,
        CreateConversationResponse500,
    ]
]:
    """Create a new conversation.

     Create a new conversation for a project identified by its unique projectId. This endpoint allows you
    to initiate a new conversation within a specific project. A conversation serves as a platform for
    users to exchange messages regarding project-related matters. By providing the projectId, you can
    establish a conversation within the context of the project allowing you to seamlessly communicate
    with it.
    Here is an example to create a conversation: [API](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/Create_a_new_conversation_and_send_a_message_to_the_conversation.ipynb)
    [SDK](https://github.com/Poll-The-People/customgpt-cookbook/blob/main/examples/SDK_Create_a_new_conv
    ersation_and_send_a_message_to_the_conversation.ipynb).

    Args:
        project_id (int):
        json_body (CreateConversationJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateConversationResponse201, CreateConversationResponse400, CreateConversationResponse401, CreateConversationResponse404, CreateConversationResponse500]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
