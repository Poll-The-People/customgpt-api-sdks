import pytest

from customgpt_client import CustomGPT
from tests.credentials import credentials


def test_sync_pages():
    CustomGPT.base_url, CustomGPT.api_key = credentials()
    CustomGPT.timeout = 10000
    response = CustomGPT.Project.create(
        project_name="test",
        sitemap_path="https://adorosario.github.io/small-sitemap.xml",
    )
    response_create = response.parsed
    project_id = response_create.data["id"]
    response = CustomGPT.Page.get(project_id=project_id)
    assert response.status_code == 200
    response_page = response.parsed
    if len(response_page.data.pages.data) > 0:
        page_id = response_page.data.pages.data[0].id
        response = CustomGPT.Page.reindex(project_id=project_id, page_id=page_id)
        assert response.parsed.data.updated
        assert response.status_code == 200
        response = CustomGPT.Page.delete(project_id=project_id, page_id=page_id)
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_async_pages():
    CustomGPT.base_url, CustomGPT.api_key = credentials()

    CustomGPT.timeout = 10000
    response = await CustomGPT.Project.acreate(
        project_name="test",
        sitemap_path="https://adorosario.github.io/small-sitemap.xml",
    )
    response_create = response.parsed
    project_id = response_create.data.id
    response = await CustomGPT.Page.aget(project_id=project_id)
    response_page = response.parsed
    if len(response_page.data.pages.data) > 0:
        page_id = response_page.data.pages.data[0].id
        response = CustomGPT.Page.reindex(project_id=project_id, page_id=page_id)
        assert response.parsed.data.updated
        assert response.status_code == 200
        response = await CustomGPT.Page.adelete(project_id=project_id, page_id=page_id)
        assert response.status_code == 200
