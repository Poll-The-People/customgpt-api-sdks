import pytest

from custom_gpt_client import CustomGPT


def test_project_settings():
    CustomGPT.base_url = "https://dev.customgpt.ai"
    CustomGPT.api_key = ""
    CustomGPT.timeout = 10000
    response = CustomGPT.Project.create(
        project_name="test", sitemap_path="https://adorosario.github.io/small-sitemap.xml"
    )
    response_create = response.parsed
    project_id = response_create.data.id
    response = CustomGPT.ProjectSettings.update(
        project_id=project_id,
        default_prompt="Hello World",
        example_questions=["Who are you?"],
        response_source="test",
        chatbot_msg_lang="ur",
    )
    assert response.status_code == 200
    response = CustomGPT.ProjectSettings.get(project_id=project_id)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_project_settings():
    CustomGPT.base_url = "https://dev.customgpt.ai"
    CustomGPT.api_key = ""
    CustomGPT.timeout = 10000
    response = await CustomGPT.Project.acreate(
        project_name="test", sitemap_path="https://adorosario.github.io/small-sitemap.xml"
    )
    response_create = response.parsed
    project_id = response_create.data.id
    response = await CustomGPT.ProjectSettings.aupdate(
        project_id=project_id, default_prompt="Hello World", example_questions=["Who are you?"], chatbot_msg_lang="ur"
    )
    assert response.status_code == 200
    response = await CustomGPT.ProjectSettings.aget(project_id=project_id)
    assert response.status_code == 200
