import pytest

from customgpt_client import CustomGPT
from tests.credentials import credentials


def test_sync_page_metadata():
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
        metadata = CustomGPT.PageMetadata.get(project_id=project_id, page_id=page_id)
        assert metadata.status_code == 200
        title = metadata.parsed.data.title
        update_metadata = CustomGPT.PageMetadata.update(
            project_id=project_id, page_id=page_id, title="test"
        )
        assert update_metadata.status_code == 200
        assert update_metadata.parsed.data.title != title
        response = CustomGPT.Page.delete(project_id=project_id, page_id=page_id)
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_async_page_metadata():
    CustomGPT.base_url, CustomGPT.api_key = credentials()
    CustomGPT.timeout = 10000
    response = await CustomGPT.Project.acreate(
        project_name="test",
        sitemap_path="https://adorosario.github.io/small-sitemap.xml",
    )
    response_create = response.parsed
    project_id = response_create.data["id"]
    response = await CustomGPT.Page.aget(project_id=project_id)
    assert response.status_code == 200
    response_page = response.parsed
    if len(response_page.data.pages.data) > 0:
        page_id = response_page.data.pages.data[0].id
        metadata = await CustomGPT.PageMetadata.aget(
            project_id=project_id, page_id=page_id
        )
        assert metadata.status_code == 200
        title = metadata.parsed.data.title
        update_metadata = await CustomGPT.PageMetadata.aupdate(
            project_id=project_id, page_id=page_id, title="test"
        )
        assert update_metadata.status_code == 200
        assert update_metadata.parsed.data.title != title
        response = await CustomGPT.Page.adelete(project_id=project_id, page_id=page_id)
        assert response.status_code == 200
