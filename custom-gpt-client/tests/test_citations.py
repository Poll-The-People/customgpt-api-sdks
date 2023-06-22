import time

import pytest

from custom_gpt_client import CustomGPT


def test_citations():
    CustomGPT.base_url = "https://dev.customgpt.ai"
    CustomGPT.api_key = "13|0tozJdzYhUrQ7HojFRSFzwtMAPNJXwAbYRhaNFMB"
    CustomGPT.timeout = 10000
    response = CustomGPT.Project.create(
        project_name="test", sitemap_path="https://adorosario.github.io/small-sitemap.xml"
    )
    response_create = response.parsed
    project_id = response_create.data["id"]
    response = CustomGPT.Conversation.create(project_id=project_id, name="test_converation")
    response_create = response.parsed
    session_id = response_create.data["session_id"]
    assert response_create.data["name"] == "test_converation"
    assert response.status_code == 201

    # wait for chat active
    is_chat_active = 0
    json_project = {}
    while not is_chat_active:
        response_project = CustomGPT.Project.get(project_id=project_id)
        json_project = response_project.parsed
        is_chat_active = json_project.data.is_chat_active
        time.sleep(5)

    assert json_project.data.is_chat_active == 1
    response = CustomGPT.Conversation.send(
        project_id=project_id, session_id=session_id, prompt="Who is Tom? I need a short answer in 10 words."
    )
    citation_id = response.parsed.data.citations[0]

    response = CustomGPT.Citation.get(project_id=project_id, citation_id=citation_id)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_citations():
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
    assert response_create.data.name == "test_converation"
    assert response.status_code == 201

    # wait for chat active
    is_chat_active = 0
    json_project = {}
    while not is_chat_active:
        response_project = await CustomGPT.Project.aget(project_id=project_id)
        json_project = response_project.parsed
        is_chat_active = json_project.data.is_chat_active
        time.sleep(5)

    assert json_project.data.is_chat_active == 1
    response = await CustomGPT.Conversation.asend(
        project_id=project_id, session_id=session_id, prompt="Who is Tom? I need a short answer in 10 words."
    )
    citation_id = response.parsed.data.citations[0]

    response = await CustomGPT.Citation.aget(project_id=project_id, citation_id=citation_id)
    assert response.status_code == 200
