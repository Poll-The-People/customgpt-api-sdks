import pytest

from customgpt_client import CustomGPT
from tests.credentials import credentials


def test_sync_project_settings():
    CustomGPT.base_url, CustomGPT.api_key = credentials()

    CustomGPT.timeout = 10000
    response = CustomGPT.Project.create(
        project_name="test", sitemap_path="https://adorosario.github.io/small-sitemap.xml"
    )
    response_create = response.parsed
    project_id = response_create.data.id
    response = CustomGPT.ProjectSettings.get(project_id=project_id)
    default_prompt = response.parsed.data.default_prompt
    assert response.status_code == 200
    response_update = CustomGPT.ProjectSettings.update(
        project_id=project_id,
        default_prompt="Hello World",
        example_questions=["Who are you?"],
        response_source="default",
        chatbot_msg_lang="ur",
        persona_instructions="You Are test chatbot created from a pytest",
        is_loading_indicator_enabled=False,
        enable_citations=False,
    )
    assert response_update.status_code == 200
    response = CustomGPT.ProjectSettings.get(project_id=project_id)
    assert response.status_code == 200
    assert default_prompt != response.parsed.data.default_prompt


@pytest.mark.asyncio
async def test_async_project_settings():
    CustomGPT.base_url, CustomGPT.api_key = credentials()

    CustomGPT.timeout = 10000
    response = await CustomGPT.Project.acreate(
        project_name="test", sitemap_path="https://adorosario.github.io/small-sitemap.xml"
    )
    response_create = response.parsed
    project_id = response_create.data.id
    response = await CustomGPT.ProjectSettings.aget(project_id=project_id)
    default_prompt = response.parsed.data.default_prompt
    assert response.status_code == 200
    response_update = await CustomGPT.ProjectSettings.aupdate(
        project_id=project_id,
        default_prompt="Hello World",
        example_questions=["Who are you?"],
        response_source="default",
        chatbot_msg_lang="ur",
        persona_instructions="You Are test chatbot created from a pytest",
        is_loading_indicator_enabled=False,
        enable_citations=False,
    )
    assert response_update.status_code == 200
    response = await CustomGPT.ProjectSettings.aget(project_id=project_id)
    assert response.status_code == 200
    assert default_prompt != response.parsed.data.default_prompt
