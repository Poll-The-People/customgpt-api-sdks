import pytest

from custom_gpt_client import CustomGPT


def test_projects():
    CustomGPT.base_url = "https://dev.customgpt.ai"
    CustomGPT.api_key = "13|0tozJdzYhUrQ7HojFRSFzwtMAPNJXwAbYRhaNFMB"
    CustomGPT.timeout = 10000
    response = CustomGPT.Project.create(
        project_name="test", sitemap_path="https://adorosario.github.io/small-sitemap.xml"
    )
    response_create = response.parsed
    assert response_create.data.project_name == "test"
    assert response.status_code == 201

    response = CustomGPT.Project.update(
        project_id=response_create.data.id,
        project_name="test2",
        sitemap_path="https://adorosario.github.io/small-sitemap.xml",
    )
    response_update = response.parsed
    assert response_update.data.project_name == "test2"
    assert response.status_code == 200

    # Get Project By created project Id and assert updated name
    response = CustomGPT.Project.get(project_id=response_create.data.id)
    response_project = response.parsed
    assert response_project.data.project_name == response_update.data.project_name
    assert response.status_code == 200

    # Fetch Created project Stat
    response = CustomGPT.Project.stats(project_id=response_create.data.id)
    response_stats = response.parsed
    assert response.status_code == 200
    print(response_stats.to_dict())
    assert set(list(response_stats.data.to_dict().keys())) == set(
        [
            "pages_found",
            "pages_crawled",
            "pages_indexed",
            "crawl_credits_used",
            "query_credits_used",
            "total_queries",
            "total_words_indexed",
        ]
    )
    response = CustomGPT.Project.list()
    assert response.status_code == 200

    # Delete the project
    response = CustomGPT.Project.delete(project_id=response_create.data.id)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_projects():
    CustomGPT.base_url = "https://dev.customgpt.ai"
    CustomGPT.api_key = ""
    CustomGPT.timeout = 10000
    response = await CustomGPT.Project.acreate(
        project_name="test", sitemap_path="https://adorosario.github.io/small-sitemap.xml"
    )
    response_create = response.parsed
    assert response_create.data.project_name == "test"
    assert response.status_code == 201

    response = await CustomGPT.Project.aupdate(
        project_id=response_create.data.id,
        project_name="test2",
        sitemap_path="https://adorosario.github.io/small-sitemap.xml",
    )
    response_update = response.parsed
    assert response_update.data.project_name == "test2"
    assert response.status_code == 200

    # Get Project By created project Id and assert updated name
    response = await CustomGPT.Project.aget(project_id=response_create.data.id)
    response_project = response.parsed
    assert response_project.data.project_name == response_update.data.project_name
    assert response.status_code == 200

    # Fetch Created project Stat
    response = await CustomGPT.Project.astats(project_id=response_create.data.id)
    response_stats = response.parsed
    assert response.status_code == 200

    assert set(list(response_stats.data.to_dict().keys())) == set(
        [
            "pages_found",
            "pages_crawled",
            "pages_indexed",
            "crawl_credits_used",
            "query_credits_used",
            "total_queries",
            "total_words_indexed",
        ]
    )
    response = await CustomGPT.Project.alist()
    assert response.status_code == 200

    # Delete the project
    response = await CustomGPT.Project.adelete(project_id=response_create.data.id)
    assert response.status_code == 200
