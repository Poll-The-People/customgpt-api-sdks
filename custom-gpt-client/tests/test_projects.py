import json

import pytest

from custom_gpt_client import CustomGPT


def test_projects():
    client = CustomGPT(
        base_url="https://dev.customgpt.ai", token="", timeout=10000
    )
    response = client.create_project(project_name="test", sitemap_path="https://adorosario.github.io/small-sitemap.xml")
    response_create = json.loads(response.content.decode("utf-8"))
    assert response_create["data"]["project_name"] == "test"
    assert response.status_code == 201

    response = client.update_project(
        project_id=response_create["data"]["id"],
        project_name="test2",
        sitemap_path="https://adorosario.github.io/small-sitemap.xml",
    )
    response_update = json.loads(response.content.decode("utf-8"))
    assert response_update["data"]["project_name"] == "test2"
    assert response.status_code == 200

    # Get Project By created project Id and assert updated name
    response = client.get_project(project_id=response_create["data"]["id"])
    response_project = json.loads(response.content.decode("utf-8"))
    assert response_project["data"]["project_name"] == response_update["data"]["project_name"]
    assert response.status_code == 200

    # Fetch Created project Stat
    response = client.get_project_stats(project_id=response_create["data"]["id"])
    response_stats = json.loads(response.content.decode("utf-8"))
    assert response.status_code == 200
    assert list(response_stats["data"].keys()) == [
        "pages_found",
        "pages_crawled",
        "pages_indexed",
        "crawl_credits_used",
        "query_credits_used",
        "total_queries",
        "total_words_indexed",
    ]
    response = client.list_projects()
    assert response.status_code == 200

    # Delete the project
    response = client.delete_project(project_id=response_create["data"]["id"])
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_projects():
    client = CustomGPT(
        base_url="https://dev.customgpt.ai", token="", timeout=10000
    )
    response = await client.acreate_project(
        project_name="test", sitemap_path="https://adorosario.github.io/small-sitemap.xml"
    )
    response_create = json.loads(response.content.decode("utf-8"))
    assert response_create["data"]["project_name"] == "test"
    assert response.status_code == 201

    response = await client.aupdate_project(
        project_id=response_create["data"]["id"],
        project_name="test2",
        sitemap_path="https://adorosario.github.io/small-sitemap.xml",
    )
    response_update = json.loads(response.content.decode("utf-8"))
    assert response_update["data"]["project_name"] == "test2"
    assert response.status_code == 200

    # Get Project By created project Id and assert updated name
    response = await client.aget_project(project_id=response_create["data"]["id"])
    response_project = json.loads(response.content.decode("utf-8"))
    assert response_project["data"]["project_name"] == response_update["data"]["project_name"]
    assert response.status_code == 200

    # Fetch Created project Stat
    response = await client.aget_project_stats(project_id=response_create["data"]["id"])
    response_stats = json.loads(response.content.decode("utf-8"))
    assert response.status_code == 200
    assert list(response_stats["data"].keys()) == [
        "pages_found",
        "pages_crawled",
        "pages_indexed",
        "crawl_credits_used",
        "query_credits_used",
        "total_queries",
        "total_words_indexed",
    ]
    response = await client.alist_projects()
    assert response.status_code == 200

    # Delete the project
    response = await client.adelete_project(project_id=response_create["data"]["id"])
    assert response.status_code == 200
