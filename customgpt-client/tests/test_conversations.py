import time
import pytest
from customgpt_client import CustomGPT
from tests.credentials import credentials


def test_sync_conversations():
    CustomGPT.base_url, CustomGPT.api_key = credentials()

    CustomGPT.timeout = 10000
    response = CustomGPT.Project.create(
        project_name="test", sitemap_path="https://adorosario.github.io/small-sitemap.xml"
    )
    response_create = response.parsed
    project_id = response_create.data.id
    response = CustomGPT.Conversation.create(project_id=project_id, name="test_converation")
    response_create = response.parsed
    session_id = response_create.data.session_id
    assert response_create.data.name == "test_converation"
    assert response.status_code == 201

    # # wait for chat active
    is_chat_active = 0
    json_project = {}
    while not is_chat_active:
        response_project = CustomGPT.Project.get(project_id=project_id)
        json_project = response_project.parsed
        is_chat_active = json_project.data.is_chat_active
        time.sleep(5)

    assert json_project.data.is_chat_active == 1

    # Get Project By created project Id and assert updated name
    response = CustomGPT.Conversation.get(project_id=project_id)
    response_conversation = response.parsed
    assert len(response_conversation.data.data) > 0

    # assert response_project['data']['name'] == 'test_conversation2'
    assert response.status_code == 200

    # send message to conversation stream false
    response = CustomGPT.Conversation.send(
        project_id=project_id, session_id=session_id, prompt="Who is Tom? I need a short answer in 10 words."
    )
    assert response.status_code == 200

    # Fetch Created project messages
    response = CustomGPT.Conversation.messages(project_id=project_id, session_id=session_id)
    response_messages = response.parsed
    assert response.status_code == 200
    assert len(response_messages.data.messages.data) > 0
    # send message to conversation stream true
    response = CustomGPT.Conversation.send(
        project_id=project_id,
        session_id=session_id,
        prompt="Who is Tom? I need a short answer in 10 words.",
        stream=True,
    )
    array = []
    for chunk in response.events():
        array.append(chunk)
    assert len(array) > 1

    # send message to conversation false
    response = CustomGPT.Conversation.send(
        project_id=project_id, session_id=session_id, prompt="Who is Tom? I need a short answer in 10 words."
    )
    assert response.status_code == 200

    # Delete the project
    response = CustomGPT.Conversation.delete(project_id=project_id, session_id=session_id)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_async_conversations():
    CustomGPT.base_url, CustomGPT.api_key = credentials()

    CustomGPT.timeout = 10000
    response = await CustomGPT.Project.acreate(
        project_name="test", sitemap_path="https://adorosario.github.io/small-sitemap.xml"
    )
    response_create = response.parsed
    project_id = response_create.data.id
    response = await CustomGPT.Conversation.acreate(project_id=project_id, name="test_converation")
    response_create = response.parsed
    session_id = response_create.data.session_id
    assert response_create.data.name == "test_converation"
    assert response.status_code == 201

    # # wait for chat active
    is_chat_active = 0
    json_project = {}
    while not is_chat_active:
        response_project = await CustomGPT.Project.aget(project_id=project_id)
        json_project = response_project.parsed
        is_chat_active = json_project.data.is_chat_active
        time.sleep(5)

    assert json_project.data.is_chat_active == 1

    # Get Conversations of project
    response = await CustomGPT.Conversation.aget(project_id=project_id)
    response_project = response.parsed
    assert len(response_project.data.data) > 0
    assert response.status_code == 200

    response = await CustomGPT.Conversation.aupdate(
        project_id=project_id, session_id=session_id, name="test_conversation2"
    )
    response_project = response.parsed
    assert response_project.data.name == "test_conversation2"
    assert response.status_code == 200

    # send message to conversation stream false
    response = await CustomGPT.Conversation.asend(
        project_id=project_id, session_id=session_id, prompt="Who is Tom? I need a short answer in 10 words."
    )
    assert response.status_code == 200

    # Fetch Created project messages
    response = await CustomGPT.Conversation.amessages(project_id=project_id, session_id=session_id)
    assert response.status_code == 200

    # Delete the project
    response = await CustomGPT.Conversation.adelete(project_id=project_id, session_id=session_id)
    assert response.status_code == 200
