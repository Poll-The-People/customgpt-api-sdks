import json
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import requests

from ... import errors
from ...models.messages_conversation_order import MessagesConversationOrder
from ...models.messages_conversation_response_200 import MessagesConversationResponse200
from ...models.messages_conversation_response_400 import MessagesConversationResponse400
from ...models.messages_conversation_response_401 import MessagesConversationResponse401
from ...models.messages_conversation_response_404 import MessagesConversationResponse404
from ...models.messages_conversation_response_500 import MessagesConversationResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: int,
    session_id: str,
    *,
    client: {},
    page: Union[Unset, None, int] = 1,
    order: Union[Unset, None, MessagesConversationOrder] = MessagesConversationOrder.DESC,
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectId}/conversations/{sessionId}/messages".format(
        client.base_url, projectId=project_id, sessionId=session_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    json_order: Union[Unset, None, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value if order else None

    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "allow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(
    *, client: {}, response: None
) -> Optional[
    Union[
        MessagesConversationResponse200,
        MessagesConversationResponse400,
        MessagesConversationResponse401,
        MessagesConversationResponse404,
        MessagesConversationResponse500,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = MessagesConversationResponse200.from_dict(json.loads(response.text))

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = MessagesConversationResponse400.from_dict(json.loads(response.text))

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = MessagesConversationResponse401.from_dict(json.loads(response.text))

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = MessagesConversationResponse404.from_dict(json.loads(response.text))

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = MessagesConversationResponse500.from_dict(json.loads(response.text))

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: {}, response: None, content: Optional[bytes] = None
) -> Response[
    Union[
        MessagesConversationResponse200,
        MessagesConversationResponse400,
        MessagesConversationResponse401,
        MessagesConversationResponse404,
        MessagesConversationResponse500,
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
    page: Union[Unset, None, int] = 1,
    order: Union[Unset, None, MessagesConversationOrder] = MessagesConversationOrder.DESC,
):
    """Retrieve messages that have been sent in a conversation.

     Retrieve all messages sent within a conversation of a project identified by its unique projectId and
    sessionId. This endpoint allows you to retrieve a collection of messages exchanged in a specific
    conversation. Messages contain the content, timestamps, and other relevant information shared during
    the course of the conversation. By providing the projectId and sessionId, you can access all the
    messages associated with that particular conversation within the project context.
    Here is an example to retrieve messages of a conversation: [API](https://github.com/Poll-The-
    People/customgpt-cookbook/blob/main/examples/Retrieve_messages_for_a_conversation.ipynb)
    [SDK](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/SDK_Retrieve_Messages_of_conversation.ipynb).

    Args:
        project_id (int):  Example: 1.
        session_id (str):  Example: 1.
        page (Union[Unset, None, int]):  Default: 1.
        order (Union[Unset, None, MessagesConversationOrder]):  Default:
            MessagesConversationOrder.DESC. Example: desc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[MessagesConversationResponse200, MessagesConversationResponse400, MessagesConversationResponse401, MessagesConversationResponse404, MessagesConversationResponse500]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        session_id=session_id,
        client=client,
        page=page,
        order=order,
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
    page: Union[Unset, None, int] = 1,
    order: Union[Unset, None, MessagesConversationOrder] = MessagesConversationOrder.DESC,
) -> Optional[
    Union[
        MessagesConversationResponse200,
        MessagesConversationResponse400,
        MessagesConversationResponse401,
        MessagesConversationResponse404,
        MessagesConversationResponse500,
    ]
]:
    """Retrieve messages that have been sent in a conversation.

     Retrieve all messages sent within a conversation of a project identified by its unique projectId and
    sessionId. This endpoint allows you to retrieve a collection of messages exchanged in a specific
    conversation. Messages contain the content, timestamps, and other relevant information shared during
    the course of the conversation. By providing the projectId and sessionId, you can access all the
    messages associated with that particular conversation within the project context.
    Here is an example to retrieve messages of a conversation: [API](https://github.com/Poll-The-
    People/customgpt-cookbook/blob/main/examples/Retrieve_messages_for_a_conversation.ipynb)
    [SDK](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/SDK_Retrieve_Messages_of_conversation.ipynb).

    Args:
        project_id (int):  Example: 1.
        session_id (str):  Example: 1.
        page (Union[Unset, None, int]):  Default: 1.
        order (Union[Unset, None, MessagesConversationOrder]):  Default:
            MessagesConversationOrder.DESC. Example: desc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[MessagesConversationResponse200, MessagesConversationResponse400, MessagesConversationResponse401, MessagesConversationResponse404, MessagesConversationResponse500]
    """

    return sync_detailed(
        project_id=project_id,
        session_id=session_id,
        client=client,
        page=page,
        order=order,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    session_id: str,
    *,
    client: {},
    page: Union[Unset, None, int] = 1,
    order: Union[Unset, None, MessagesConversationOrder] = MessagesConversationOrder.DESC,
) -> Response[
    Union[
        MessagesConversationResponse200,
        MessagesConversationResponse400,
        MessagesConversationResponse401,
        MessagesConversationResponse404,
        MessagesConversationResponse500,
    ]
]:
    kwargs = _get_kwargs(
        project_id=project_id,
        session_id=session_id,
        client=client,
        page=page,
        order=order,
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
    page: Union[Unset, None, int] = 1,
    order: Union[Unset, None, MessagesConversationOrder] = MessagesConversationOrder.DESC,
) -> Optional[
    Union[
        MessagesConversationResponse200,
        MessagesConversationResponse400,
        MessagesConversationResponse401,
        MessagesConversationResponse404,
        MessagesConversationResponse500,
    ]
]:
    """Retrieve messages that have been sent in a conversation.

     Retrieve all messages sent within a conversation of a project identified by its unique projectId and
    sessionId. This endpoint allows you to retrieve a collection of messages exchanged in a specific
    conversation. Messages contain the content, timestamps, and other relevant information shared during
    the course of the conversation. By providing the projectId and sessionId, you can access all the
    messages associated with that particular conversation within the project context.
    Here is an example to retrieve messages of a conversation: [API](https://github.com/Poll-The-
    People/customgpt-cookbook/blob/main/examples/Retrieve_messages_for_a_conversation.ipynb)
    [SDK](https://github.com/Poll-The-People/customgpt-
    cookbook/blob/main/examples/SDK_Retrieve_Messages_of_conversation.ipynb).

    Args:
        project_id (int):  Example: 1.
        session_id (str):  Example: 1.
        page (Union[Unset, None, int]):  Default: 1.
        order (Union[Unset, None, MessagesConversationOrder]):  Default:
            MessagesConversationOrder.DESC. Example: desc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[MessagesConversationResponse200, MessagesConversationResponse400, MessagesConversationResponse401, MessagesConversationResponse404, MessagesConversationResponse500]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            session_id=session_id,
            client=client,
            page=page,
            order=order,
        )
    ).parsed
