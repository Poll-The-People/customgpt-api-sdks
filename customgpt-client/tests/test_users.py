import pytest

from customgpt_client import CustomGPT
from tests.credentials import credentials


def test_sync_users():
    CustomGPT.base_url, CustomGPT.api_key = credentials()
    CustomGPT.timeout = 10000
    response = CustomGPT.Project.create(
        project_name="test", sitemap_path="https://adorosario.github.io/small-sitemap.xml"
    )
    response_create = response.parsed
    response_create.data.id
    response = CustomGPT.User.get()
    assert response.status_code == 200
    response = CustomGPT.User.update(name="Hamza 2")
    response_json = response.parsed
    assert response.status_code == 200
    assert response_json.data.name == "Hamza 2"


@pytest.mark.asyncio
async def test_async_users():
    CustomGPT.base_url, CustomGPT.api_key = credentials()
    CustomGPT.timeout = 10000
    response = await CustomGPT.Project.acreate(
        project_name="test", sitemap_path="https://adorosario.github.io/small-sitemap.xml"
    )
    response_create = response.parsed
    response_create.data.id
    response = await CustomGPT.User.aget()
    assert response.status_code == 200
    response = await CustomGPT.User.aupdate(name="Hamza 3")
    response_json = response.parsed
    assert response.status_code == 200
    assert response_json.data.name == "Hamza 3"
