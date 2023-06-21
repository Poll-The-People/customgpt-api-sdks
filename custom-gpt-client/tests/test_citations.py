import json
import time

import pytest

from custom_gpt_client import CustomGPT


def test_citations():
    client = CustomGPT(base_url="https://dev.customgpt.ai", token="", timeout=10000)
    response = client.create_project(project_name="test", sitemap_path="https://adorosario.github.io/small-sitemap.xml")
    response_create = json.loads(response.content.decode("utf-8"))
    project_id = response_create["data"]["id"]
    response = client.create_project_conversations(project_id=project_id, name="test_converation")
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
    response = client.send_message_to_conversation(
        project_id=project_id, session_id=session_id, prompt="Who is Tom? I need a short answer in 10 words."
    )
    citation_id = json.loads(response.content.decode("utf-8"))["data"]["citations"][0]

    response = client.get_open_graph_data_for_citation(project_id=project_id, citation_id=citation_id)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_citations():
    client = CustomGPT(base_url="https://dev.customgpt.ai", token="", timeout=10000)
    response = await client.acreate_project(
        project_name="test", sitemap_path="https://adorosario.github.io/small-sitemap.xml"
    )
    response_create = json.loads(response.content.decode("utf-8"))
    project_id = response_create["data"]["id"]
    response = await client.acreate_project_conversations(project_id=project_id, name="test_converation")
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
    response = await client.asend_message_to_conversation(
        project_id=project_id, session_id=session_id, prompt="Who is Tom? I need a short answer in 10 words."
    )
    citation_id = json.loads(response.content.decode("utf-8"))["data"]["citations"][0]

    response = await client.aget_open_graph_data_for_citation(project_id=project_id, citation_id=citation_id)
    assert response.status_code == 200
