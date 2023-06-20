import json

import pytest

from custom_gpt_client import CustomGPT


def test_users():
    client = CustomGPT(
        base_url="https://dev.customgpt.ai", token="", timeout=10000
    )
    response = client.create_project(project_name="test", sitemap_path="https://adorosario.github.io/small-sitemap.xml")
    response_create = json.loads(response.content.decode("utf-8"))
    response_create["data"]["id"]
    response = client.get_user_profile()
    assert response.status_code == 200
    response = client.update_user_profile(name="Hamza 2")
    response_json = response.parsed
    assert response.status_code == 200
    assert response_json["data"]["name"] == "Hamza 2"


@pytest.mark.asyncio
async def test_users():
    client = CustomGPT(
        base_url="https://dev.customgpt.ai", token="", timeout=10000
    )
    response = await client.acreate_project(
        project_name="test", sitemap_path="https://adorosario.github.io/small-sitemap.xml"
    )
    response_create = json.loads(response.content.decode("utf-8"))
    response_create["data"]["id"]
    response = await client.aget_user_profile()
    assert response.status_code == 200
    response = await client.aupdate_user_profile(name="Hamza 3")
    response_json = json.loads(response.content.decode("utf-8"))
    assert response.status_code == 200
    assert response_json["data"]["name"] == "Hamza 3"
