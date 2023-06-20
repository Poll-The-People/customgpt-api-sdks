import json
import pytest
from custom_gpt_client import CustomGPT

def test_project_settings():
    client = CustomGPT(
        base_url="https://dev.customgpt.ai", token="", timeout=10000
    )
    response = client.create_project(project_name="test", sitemap_path="https://adorosario.github.io/small-sitemap.xml")
    response_create = json.loads(response.content.decode("utf-8"))
    project_id = response_create["data"]["id"]
    response = client.update_project_settings(
        project_id=project_id,
        default_prompt="Hello World",
        example_questions=["Who are you?"],
        response_source="test",
        chatbot_msg_lang="urdu",
    )
    assert response.status_code == 200
    response = client.get_project_settings(project_id=project_id)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_project_settings():
    client = CustomGPT(
        base_url="https://dev.customgpt.ai", token="", timeout=10000
    )
    response = await client.acreate_project(project_name="test", sitemap_path="https://adorosario.github.io/small-sitemap.xml")
    response_create = json.loads(response.content.decode("utf-8"))
    project_id = response_create["data"]["id"]
    response = await client.aupdate_project_settings(project_id=project_id, default_prompt='Hello World', example_questions=['Who are you?'], chatbot_msg_lang='ur')
    assert response.status_code == 200
    response = await client.aget_project_settings(project_id=project_id)
    assert response.status_code == 200
