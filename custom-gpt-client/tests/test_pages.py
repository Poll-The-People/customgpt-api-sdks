import json
import pytest
from custom_gpt_client import CustomGPT


def test_pages():
    client = CustomGPT(
        base_url="https://dev.customgpt.ai", token="", timeout=10000
    )
    response = client.create_project(project_name="test", sitemap_path="https://adorosario.github.io/small-sitemap.xml")
    response_create = json.loads(response.content.decode("utf-8"))
    project_id = response_create["data"]["id"]
    response = client.get_project_pages(project_id=project_id)
    assert response.status_code == 200
    response_page = json.loads(response.content.decode("utf-8"))
    page_id = response_page["data"]["pages"]["data"][0]["id"]
    assert response.status_code == 200
    response = client.delete_project_page(project_id=project_id, page_id=page_id)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_pages():
    client = CustomGPT(
        base_url="https://dev.customgpt.ai", token="", timeout=10000
    )
    response = await client.acreate_project(
        project_name="test", sitemap_path="https://adorosario.github.io/small-sitemap.xml"
    )
    response_create = json.loads(response.content.decode("utf-8"))
    project_id = response_create["data"]["id"]
    response = await client.aget_project_pages(project_id=project_id)
    response_page = json.loads(response.content.decode("utf-8"))
    if len(response_page["data"]["pages"]["data"]) > 0:
        page_id = response_page["data"]["pages"]["data"][0]["id"]
        assert response.status_code == 200
        response = await client.adelete_project_page(project_id=project_id, page_id=page_id)
        assert response.status_code == 200
