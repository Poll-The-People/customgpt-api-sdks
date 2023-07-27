import json
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import requests
from sseclient import SSEClient

from ... import errors
from ...models.send_message_json_body import SendMessageJsonBody
from ...models.send_message_response_200 import SendMessageResponse200
from ...models.send_message_response_400 import SendMessageResponse400
from ...models.send_message_response_401 import SendMessageResponse401
from ...models.send_message_response_404 import SendMessageResponse404
from ...models.send_message_response_500 import SendMessageResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: int,
    session_id: str,
    *,
    client: {},
    json_body: SendMessageJsonBody,
    stream: Union[Unset, None, bool] = False,
    lang: Union[Unset, None, str] = "en",
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectId}/conversations/{sessionId}/messages".format(
        client.base_url, projectId=project_id, sessionId=session_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["stream"] = 1 if stream else 0

    params["lang"] = lang

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    if stream:
        headers["Accept"] = "text/event-stream"

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "allow_redirects": client.follow_redirects,
        "json": json_json_body,
        "params": params,
        "stream": stream,
    }


def _parse_response(
    *, client: {}, response: None
) -> Optional[
    Union[
        SendMessageResponse200,
        SendMessageResponse400,
        SendMessageResponse401,
        SendMessageResponse404,
        SendMessageResponse500,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SendMessageResponse200.from_dict(json.loads(response.text))

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = SendMessageResponse400.from_dict(json.loads(response.text))

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = SendMessageResponse401.from_dict(json.loads(response.text))

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = SendMessageResponse404.from_dict(json.loads(response.text))

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = SendMessageResponse500.from_dict(json.loads(response.text))

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: {}, response: None, content: Optional[bytes] = None
) -> Response[
    Union[
        SendMessageResponse200,
        SendMessageResponse400,
        SendMessageResponse401,
        SendMessageResponse404,
        SendMessageResponse500,
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
    json_body: SendMessageJsonBody,
    stream: Union[Unset, None, bool] = False,
    lang: Union[Unset, None, str] = "en",
):
    """Send a message to a conversation.

     Send a message to a conversation within a project identified by its unique projectId and sessionId.
    This endpoint enables you to send a new message to a specific conversation, facilitating seamless
    communication and collaboration within the project. By providing the projectId and sessionId, you
    can target the desired conversation and contribute to the ongoing discussion. This API endpoint
    supports real-time streaming, allowing for instant message delivery and dynamic updates which
    enables efficient and interactive communication between the user and chatbot.
    Here is an example to send a message to a conversation: [API](https://github.com/Poll-The-
    People/customgpt-
    cookbook/blob/main/examples/Create_a_new_conversation_and_send_a_message_to_the_conversation.ipynb)
    [SDK](https://github.com/Poll-The-People/customgpt-cookbook/blob/main/examples/SDK_Create_a_new_conv
    ersation_and_send_a_message_to_the_conversation.ipynb).

    Args:
        project_id (int):  Example: 1.
        session_id (str):  Example: 1.
        stream (Union[Unset, None, bool]):
        lang (Union[Unset, None, str]):  Default: 'en'.
        json_body (SendMessageJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SendMessageResponse200, SendMessageResponse400, SendMessageResponse401, SendMessageResponse404, SendMessageResponse500]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        session_id=session_id,
        client=client,
        json_body=json_body,
        stream=stream,
        lang=lang,
    )

    response = requests.request(
        **kwargs,
    )

    if stream:
        return SSEClient(response)
    else:
        return _build_response(client=client, response=response)


def sync(
    project_id: int,
    session_id: str,
    *,
    client: {},
    json_body: SendMessageJsonBody,
    stream: Union[Unset, None, bool] = False,
    lang: Union[Unset, None, str] = "en",
) -> Optional[
    Union[
        SendMessageResponse200,
        SendMessageResponse400,
        SendMessageResponse401,
        SendMessageResponse404,
        SendMessageResponse500,
    ]
]:
    """Send a message to a conversation.

     Send a message to a conversation within a project identified by its unique projectId and sessionId.
    This endpoint enables you to send a new message to a specific conversation, facilitating seamless
    communication and collaboration within the project. By providing the projectId and sessionId, you
    can target the desired conversation and contribute to the ongoing discussion. This API endpoint
    supports real-time streaming, allowing for instant message delivery and dynamic updates which
    enables efficient and interactive communication between the user and chatbot.
    Here is an example to send a message to a conversation: [API](https://github.com/Poll-The-
    People/customgpt-
    cookbook/blob/main/examples/Create_a_new_conversation_and_send_a_message_to_the_conversation.ipynb)
    [SDK](https://github.com/Poll-The-People/customgpt-cookbook/blob/main/examples/SDK_Create_a_new_conv
    ersation_and_send_a_message_to_the_conversation.ipynb).

    Args:
        project_id (int):  Example: 1.
        session_id (str):  Example: 1.
        stream (Union[Unset, None, bool]):
        lang (Union[Unset, None, str]):  Default: 'en'.
        json_body (SendMessageJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SendMessageResponse200, SendMessageResponse400, SendMessageResponse401, SendMessageResponse404, SendMessageResponse500]
    """

    return sync_detailed(
        project_id=project_id,
        session_id=session_id,
        client=client,
        json_body=json_body,
        stream=stream,
        lang=lang,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    session_id: str,
    *,
    client: {},
    json_body: SendMessageJsonBody,
    stream: Union[Unset, None, bool] = False,
    lang: Union[Unset, None, str] = "en",
) -> Response[
    Union[
        SendMessageResponse200,
        SendMessageResponse400,
        SendMessageResponse401,
        SendMessageResponse404,
        SendMessageResponse500,
    ]
]:
    kwargs = _get_kwargs(
        project_id=project_id,
        session_id=session_id,
        client=client,
        json_body=json_body,
        stream=stream,
        lang=lang,
    )

    response = requests.request(
        **kwargs,
    )

    if stream:
        return SSEClient(response)
    else:
        return _build_response(client=client, response=response)


async def asyncio(
    project_id: int,
    session_id: str,
    *,
    client: {},
    json_body: SendMessageJsonBody,
    stream: Union[Unset, None, bool] = False,
    lang: Union[Unset, None, str] = "en",
) -> Optional[
    Union[
        SendMessageResponse200,
        SendMessageResponse400,
        SendMessageResponse401,
        SendMessageResponse404,
        SendMessageResponse500,
    ]
]:
    """Send a message to a conversation.

     Send a message to a conversation within a project identified by its unique projectId and sessionId.
    This endpoint enables you to send a new message to a specific conversation, facilitating seamless
    communication and collaboration within the project. By providing the projectId and sessionId, you
    can target the desired conversation and contribute to the ongoing discussion. This API endpoint
    supports real-time streaming, allowing for instant message delivery and dynamic updates which
    enables efficient and interactive communication between the user and chatbot.
    Here is an example to send a message to a conversation: [API](https://github.com/Poll-The-
    People/customgpt-
    cookbook/blob/main/examples/Create_a_new_conversation_and_send_a_message_to_the_conversation.ipynb)
    [SDK](https://github.com/Poll-The-People/customgpt-cookbook/blob/main/examples/SDK_Create_a_new_conv
    ersation_and_send_a_message_to_the_conversation.ipynb).

    Args:
        project_id (int):  Example: 1.
        session_id (str):  Example: 1.
        stream (Union[Unset, None, bool]):
        lang (Union[Unset, None, str]):  Default: 'en'.
        json_body (SendMessageJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SendMessageResponse200, SendMessageResponse400, SendMessageResponse401, SendMessageResponse404, SendMessageResponse500]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            session_id=session_id,
            client=client,
            json_body=json_body,
            stream=stream,
            lang=lang,
        )
    ).parsed
