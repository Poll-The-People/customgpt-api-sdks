import pytest

from customgpt_client import CustomGPT


def test_pages():
    CustomGPT.base_url = "https://dev.customgpt.ai"
    CustomGPT.api_key = ""
    CustomGPT.timeout = 10000
    response = CustomGPT.Project.create(
        project_name="test", sitemap_path="https://adorosario.github.io/small-sitemap.xml"
    )
    response_create = response.parsed
    project_id = response_create.data["id"]
    response = CustomGPT.Page.get(project_id=project_id)
    assert response.status_code == 200
    response_page = response.parsed
    print(response_page.data.pages.data)
    page_id = response_page.data.pages.data[0].id
    assert response.status_code == 200
    response = CustomGPT.Page.delete(project_id=project_id, page_id=page_id)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_pages():
    CustomGPT.base_url = "https://dev.customgpt.ai"
    CustomGPT.api_key = ""
    CustomGPT.timeout = 10000
    response = await CustomGPT.Project.acreate(
        project_name="test", sitemap_path="https://adorosario.github.io/small-sitemap.xml"
    )
    response_create = response.parsed
    project_id = response_create.data.id
    response = await CustomGPT.Page.aget(project_id=project_id)
    response_page = response.parsed
    if len(response_page.data.pages.data) > 0:
        page_id = response_page.data.pages.data[0].id
        assert response.status_code == 200
        response = await CustomGPT.Page.adelete(project_id=project_id, page_id=page_id)
        assert response.status_code == 200
