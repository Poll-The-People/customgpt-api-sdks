import json
import time

import pytest

from custom_gpt_client import CustomGPT


def test_conversations():
    client = CustomGPT(
        base_url="https://dev.customgpt.ai", token="", timeout=10000
    )
    response = client.create_project(project_name="test", sitemap_path="https://adorosario.github.io/small-sitemap.xml")
    response_create = json.loads(response.content.decode("utf-8"))
    project_id = response_create["data"]["id"]
    response = client.create_project_conversation(project_id=project_id, name="test_converation")
    response_create = json.loads(response.content.decode("utf-8"))
    session_id = response_create["data"]["session_id"]
    assert response_create["data"]["name"] == "test_converation"
    assert response.status_code == 201

    # wait for chat active
    is_chat_active = 0
    json_project = {}
    while not is_chat_active:
        response_project = client.get_project(project_id=project_id)
        json_project = json.loads(response_project.content.decode("utf-8"))
        is_chat_active = json_project["data"]["is_chat_active"]
        time.sleep(5)

    assert json_project["data"]["is_chat_active"] == 1

    # Get Project By created project Id and assert updated name
    response = client.get_project_conversations(project_id=project_id)
    response_project = json.loads(response.content.decode("utf-8"))
    assert len(response_project["data"]) > 0

    # assert response_project['data']['name'] == 'test_conversation2'
    assert response.status_code == 200

    # Fetch Created project messages
    response = client.get_project_conversation_messages(project_id=project_id, session_id=session_id)
    json.loads(response.content.decode("utf-8"))
    assert response.status_code == 200
    assert list(response_stats["data"].keys()) == [
        "pages_found",
        "pages_crawled",
        "pages_indexed",
        "crawl_credits_used",
        "query_credits_used",
        "total_queries",
        "total_words_indexed",
    ]

    # send message to conversation stream false
    response = client.send_message_to_conversation(
        project_id=project_id, session_id=session_id, prompt="Who is Tom? I need a short answer in 10 words."
    )
    message_json = json.loads(response.content.decode("utf-8"))
    assert response.status_code == 200
    assert list(message_json["data"].keys()) == [
        "id",
        "created_at",
        "updated_at",
        "user_id",
        "user_query",
        "openai_response",
        "citations",
    ]

    # send message to conversation stream true
    response = client.send_message_to_conversation(
        project_id=project_id,
        session_id=session_id,
        prompt="Who is Tom? I need a short answer in 10 words.",
        stream=True,
    )
    for chunk in response:
        assert chunk.status_code == 200
    assert len(response) > 1

    # Delete the project
    response = client.delete_project_conversation(project_id=project_id, session_id=session_id)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_conversations():
    client = CustomGPT(
        base_url="https://dev.customgpt.ai", token="", timeout=10000
    )
    response = await client.acreate_project(
        project_name="test", sitemap_path="https://adorosario.github.io/small-sitemap.xml"
    )
    response_create = json.loads(response.content.decode("utf-8"))
    project_id = response_create["data"]["id"]
    response = await client.acreate_project_conversation(project_id=project_id, name="test_converation")
    response_create = json.loads(response.content.decode("utf-8"))
    session_id = response_create["data"]["session_id"]
    assert response_create["data"]["name"] == "test_converation"
    assert response.status_code == 201

    # wait for chat active
    is_chat_active = 0
    json_project = {}
    while not is_chat_active:
        response_project = await client.aget_project(project_id=project_id)
        json_project = json.loads(response_project.content.decode("utf-8"))
        is_chat_active = json_project["data"]["is_chat_active"]
        time.sleep(5)

    assert json_project["data"]["is_chat_active"] == 1

    # Get Project By created project Id and assert updated name
    response = await client.aget_project_conversations(project_id=project_id)
    response_project = json.loads(response.content.decode("utf-8"))
    assert len(response_project["data"]) > 0
    response = await client.aupdate_project_conversation(
        project_id=project_id, session_id=session_id, name="test_conversation2"
    )
    response_project = json.loads(response.content.decode("utf-8"))
    assert response_project["data"]["name"] == "test_conversation2"
    assert response.status_code == 200

    # Fetch Created project messages
    response = await client.aget_project_conversation_messages(project_id=project_id, session_id=session_id)
    json.loads(response.content.decode("utf-8"))
    assert response.status_code == 200
    # assert list(response_stats['data'].keys()) == ['pages_found', 'pages_crawled', 'pages_indexed', 'crawl_credits_used', 'query_credits_used', 'total_queries', 'total_words_indexed']

    # send message to conversation stream false
    response = await client.asend_message_to_conversation(
        project_id=project_id, session_id=session_id, prompt="Who is Tom? I need a short answer in 10 words."
    )
    message_json = json.loads(response.content.decode("utf-8"))
    assert response.status_code == 200
    assert list(message_json["data"].keys()) == [
        "id",
        "created_at",
        "updated_at",
        "user_id",
        "user_query",
        "openai_response",
        "citations",
    ]

    # send message to conversation stream true
    response = await client.asend_message_to_conversation(
        project_id=project_id,
        session_id=session_id,
        prompt="Who is Tom? I need a short answer in 10 words.",
        stream=True,
    )
    async for chunk in response:
        assert chunk.status_code == 200

    # Delete the project
    response = await client.adelete_project_conversation(project_id=project_id, session_id=session_id)
    assert response.status_code == 200
