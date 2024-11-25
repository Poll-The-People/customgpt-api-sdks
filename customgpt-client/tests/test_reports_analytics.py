import time

import pytest

from customgpt_client import CustomGPT
from tests.credentials import credentials


def test_sync_reports():
    CustomGPT.base_url, CustomGPT.api_key = credentials()

    response = CustomGPT.Project.create(
        project_name="test",
        sitemap_path="https://adorosario.github.io/small-sitemap.xml",
    )
    response_create = response.parsed
    project_id = response_create.data.id
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
        project_id=project_id,
        session_id=session_id,
        prompt="Who is Tom? I need a short answer in 10 words.",
    )
    assert response.status_code == 200
    response = CustomGPT.ReportsAnalytics.analysis(project_id=project_id, filters=["sources"])
    assert response.status_code == 200

    response = CustomGPT.ReportsAnalytics.conversations(project_id=project_id, filters=["sources"])
    assert response.status_code == 200

    response = CustomGPT.ReportsAnalytics.queries(project_id=project_id, filters=["sources"])
    assert response.status_code == 200

    response = CustomGPT.ReportsAnalytics.traffic(project_id=project_id, filters=["sources"])
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_async_reports():
    CustomGPT.base_url, CustomGPT.api_key = credentials()

    response = CustomGPT.Project.create(
        project_name="test",
        sitemap_path="https://adorosario.github.io/small-sitemap.xml",
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
        project_id=project_id,
        session_id=session_id,
        prompt="Who is Tom? I need a short answer in 10 words.",
    )
    assert response.status_code == 200
    response = await CustomGPT.ReportsAnalytics.aanalysis(project_id=project_id, filters=["sources"])
    assert response.status_code == 200

    response = await CustomGPT.ReportsAnalytics.aconversations(project_id=project_id, filters=["sources"])
    assert response.status_code == 200

    response = await CustomGPT.ReportsAnalytics.aqueries(project_id=project_id, filters=["sources"])
    assert response.status_code == 200

    response = await CustomGPT.ReportsAnalytics.atraffic(project_id=project_id, filters=["sources"])
    assert response.status_code == 200
