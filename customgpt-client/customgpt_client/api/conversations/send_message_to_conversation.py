import json
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import requests
from sseclient import SSEClient

from ... import errors
from ...models.send_message_to_conversation_json_body import SendMessageToConversationJsonBody
from ...models.send_message_to_conversation_response_200 import SendMessageToConversationResponse200
from ...models.send_message_to_conversation_response_401 import SendMessageToConversationResponse401
from ...models.send_message_to_conversation_response_404 import SendMessageToConversationResponse404
from ...models.send_message_to_conversation_response_500 import SendMessageToConversationResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: int,
    session_id: str,
    *,
    client: {},
    json_body: SendMessageToConversationJsonBody,
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
        SendMessageToConversationResponse200,
        SendMessageToConversationResponse401,
        SendMessageToConversationResponse404,
        SendMessageToConversationResponse500,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SendMessageToConversationResponse200.from_dict(json.loads(response.text))

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = SendMessageToConversationResponse401.from_dict(json.loads(response.text))

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = SendMessageToConversationResponse404.from_dict(json.loads(response.text))

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = SendMessageToConversationResponse500.from_dict(json.loads(response.text))

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: {}, response: None, content: Optional[bytes] = None
) -> Response[
    Union[
        SendMessageToConversationResponse200,
        SendMessageToConversationResponse401,
        SendMessageToConversationResponse404,
        SendMessageToConversationResponse500,
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
    json_body: SendMessageToConversationJsonBody,
    stream: Union[Unset, None, bool] = False,
    lang: Union[Unset, None, str] = "en",
):
    """Send a message to a conversation.

     Send a message to a conversation by `projectId` and `sessionId`.

    Args:
        project_id (int):  Example: 1.
        session_id (str):  Example: 1.
        stream (Union[Unset, None, bool]):
        lang (Union[Unset, None, str]):  Default: 'en'.
        json_body (SendMessageToConversationJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SendMessageToConversationResponse200, SendMessageToConversationResponse401, SendMessageToConversationResponse404, SendMessageToConversationResponse500]]
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
    json_body: SendMessageToConversationJsonBody,
    stream: Union[Unset, None, bool] = False,
    lang: Union[Unset, None, str] = "en",
) -> Optional[
    Union[
        SendMessageToConversationResponse200,
        SendMessageToConversationResponse401,
        SendMessageToConversationResponse404,
        SendMessageToConversationResponse500,
    ]
]:
    """Send a message to a conversation.

     Send a message to a conversation by `projectId` and `sessionId`.

    Args:
        project_id (int):  Example: 1.
        session_id (str):  Example: 1.
        stream (Union[Unset, None, bool]):
        lang (Union[Unset, None, str]):  Default: 'en'.
        json_body (SendMessageToConversationJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SendMessageToConversationResponse200, SendMessageToConversationResponse401, SendMessageToConversationResponse404, SendMessageToConversationResponse500]
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
    json_body: SendMessageToConversationJsonBody,
    stream: Union[Unset, None, bool] = False,
    lang: Union[Unset, None, str] = "en",
) -> Response[
    Union[
        SendMessageToConversationResponse200,
        SendMessageToConversationResponse401,
        SendMessageToConversationResponse404,
        SendMessageToConversationResponse500,
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
    json_body: SendMessageToConversationJsonBody,
    stream: Union[Unset, None, bool] = False,
    lang: Union[Unset, None, str] = "en",
) -> Optional[
    Union[
        SendMessageToConversationResponse200,
        SendMessageToConversationResponse401,
        SendMessageToConversationResponse404,
        SendMessageToConversationResponse500,
    ]
]:
    """Send a message to a conversation.

     Send a message to a conversation by `projectId` and `sessionId`.

    Args:
        project_id (int):  Example: 1.
        session_id (str):  Example: 1.
        stream (Union[Unset, None, bool]):
        lang (Union[Unset, None, str]):  Default: 'en'.
        json_body (SendMessageToConversationJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SendMessageToConversationResponse200, SendMessageToConversationResponse401, SendMessageToConversationResponse404, SendMessageToConversationResponse500]
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
