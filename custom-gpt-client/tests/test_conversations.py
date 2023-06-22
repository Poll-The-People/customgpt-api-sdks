import time

import pytest

from custom_gpt_client import CustomGPT


def test_conversations():
    CustomGPT.base_url = "https://dev.customgpt.ai"
    CustomGPT.api_key = ""
    CustomGPT.timeout = 10000
    response = CustomGPT.Project.create(
        project_name="test", sitemap_path="https://adorosario.github.io/small-sitemap.xml"
    )
    response_create = response.parsed
    project_id = response_create.data.id
    response = CustomGPT.Conversation.create(project_id=project_id, name="test_converation")
    response_create = response.parsed
    session_id = response_create.data.session_id
    # assert response_create.data.name == "test_converation"
    # assert response.status_code == 201

    # # wait for chat active
    is_chat_active = 0
    json_project = {}
    while not is_chat_active:
        response_project = CustomGPT.Project.get(project_id=project_id)
        json_project = response_project.parsed
        is_chat_active = json_project.data.is_chat_active
        time.sleep(5)

    # assert json_project.data.is_chat_active == 1

    # # Get Project By created project Id and assert updated name
    # response = CustomGPT.Conversation.get(project_id=project_id)
    # response_project = response.parsed
    # assert len(response_project.data) > 0

    # # assert response_project['data']['name'] == 'test_conversation2'
    # assert response.status_code == 200

    # # Fetch Created project messages
    # response = CustomGPT.Conversation.messages(project_id=project_id, session_id=session_id)
    # response.parsed
    # assert response.status_code == 200
    # assert list(response_stats.data.keys()) == [
    #     "pages_found",
    #     "pages_crawled",
    #     "pages_indexed",
    #     "crawl_credits_used",
    #     "query_credits_used",
    #     "total_queries",
    #     "total_words_indexed",
    # ]

    # # send message to conversation stream false
    # response = CustomGPT.Conversation.send(
    #     project_id=project_id, session_id=session_id, prompt="Who is Tom? I need a short answer in 10 words."
    # )
    # response.parsed
    # assert response.status_code == 200

    # send message to conversation stream true
    response = CustomGPT.Conversation.send(
        project_id=project_id,
        session_id=session_id,
        prompt="Who is Tom? I need a short answer in 10 words.",
        stream=True,
    )
    for chunk in response:
        assert chunk.status_code == 200
    assert len(response) > 1

    # Delete the project
    response = CustomGPT.Conversation.delete(project_id=project_id, session_id=session_id)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_conversations():
    CustomGPT.base_url = "https://dev.customgpt.ai"
    CustomGPT.api_key = ""
    CustomGPT.timeout = 10000
    response = await CustomGPT.Project.acreate(
        project_name="test", sitemap_path="https://adorosario.github.io/small-sitemap.xml"
    )
    response_create = response.parsed
    project_id = response_create.data.id
    response = await CustomGPT.Conversation.acreate(project_id=project_id, name="test_converation")
    response_create = response.parsed
    session_id = response_create.data.session_id
    # assert response_create.data.name == "test_converation"
    # assert response.status_code == 201

    # # wait for chat active
    is_chat_active = 0
    json_project = {}
    while not is_chat_active:
        response_project = await CustomGPT.Project.aget(project_id=project_id)
        json_project = response_project.parsed
        is_chat_active = json_project.data.is_chat_active
        time.sleep(5)

    # assert json_project.data.is_chat_active == 1

    # # Get Project By created project Id and assert updated name
    # response = await CustomGPT.Conversation.aget(project_id=project_id)
    # response_project = response.parsed
    # assert len(response_project.data.data) > 0
    # assert response.status_code == 200

    # response = await CustomGPT.Conversation.aupdate(
    #     project_id=project_id, session_id=session_id, name="test_conversation2"
    # )
    # response_project = response.parsed
    # assert response_project.data.name == "test_conversation2"
    # assert response.status_code == 200

    # # Fetch Created project messages
    # response = await CustomGPT.Conversation.amessages(project_id=project_id, session_id=session_id)
    # response.parsed
    # assert response.status_code == 200

    # # send message to conversation stream false
    # response = await CustomGPT.Conversation.asend(
    #     project_id=project_id, session_id=session_id, prompt="Who is Tom? I need a short answer in 10 words."
    # )
    # response.parsed
    # assert response.status_code == 200

    # send message to conversation stream true
    response = await CustomGPT.Conversation.asend(
        project_id=project_id,
        session_id=session_id,
        prompt="Who is Tom? I need a short answer in 10 words.",
        stream=True,
    )
    async for chunk in response:
        assert chunk.status_code == 200

    # Delete the project
    response = await CustomGPT.Conversation.adelete(project_id=project_id, session_id=session_id)
    assert response.status_code == 200
