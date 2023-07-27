import os
import time

import pytest

from customgpt_client import CustomGPT
from customgpt_client.types import File
from tests.credentials import credentials

current_script_path = os.path.abspath(__file__)
file_name = "file/vanka.pdf"
file_path = os.path.join(os.path.dirname(current_script_path), file_name)


def test_sync_sources():
    CustomGPT.base_url, CustomGPT.api_key = credentials()
    response = CustomGPT.Project.create(
        project_name="test", sitemap_path="https://adorosario.github.io/small-sitemap.xml"
    )
    response_create = response.parsed
    assert response_create.data.project_name == "test"
    assert response.status_code == 201
    project_id = 863
    json_project = {}
    is_chat_active = 0
    while not is_chat_active:
        response_project = CustomGPT.Project.get(project_id=project_id)
        json_project = response_project.parsed
        is_chat_active = json_project.data.is_chat_active
        time.sleep(5)

    # Add new sitemap to project using source api.
    new_sitemap_path = "https://adorosario.github.io/small-sitemap.xml"
    create_source = CustomGPT.Source.create(project_id=project_id, sitemap_path=new_sitemap_path)
    data = create_source.parsed.data
    assert data.type == "sitemap"
    assert create_source.status_code == 201

    # Add File To Project
    with open(file_path, "rb") as file:
        file_content = file.read()

    create_source = CustomGPT.Source.create(
        project_id=project_id, file=File(payload=file_content, file_name="vanka.pdf")
    )
    data = create_source.parsed.data
    assert create_source.status_code == 201
    assert data.type == "upload"

    # List Sources
    list_sources = CustomGPT.Source.list(project_id=project_id)
    data = list_sources.parsed.data
    assert list_sources.status_code == 200
    assert len(data.sitemaps) > 0

    # # Delete Source
    source_id = data.sitemaps[0].id
    delete_source = CustomGPT.Source.delete(project_id=project_id, source_id=source_id)
    assert delete_source.status_code == 200


@pytest.mark.asyncio
async def test_async_sources():
    CustomGPT.base_url, CustomGPT.api_key = credentials()
    response = await CustomGPT.Project.acreate(
        project_name="test", sitemap_path="https://adorosario.github.io/small-sitemap.xml"
    )
    response_create = response.parsed
    assert response_create.data.project_name == "test"
    assert response.status_code == 201
    project_id = 863
    json_project = {}
    is_chat_active = 0
    while not is_chat_active:
        response_project = CustomGPT.Project.get(project_id=project_id)
        json_project = response_project.parsed
        is_chat_active = json_project.data.is_chat_active
        time.sleep(5)

    # Add new sitemap to project using source api.
    new_sitemap_path = "https://adorosario.github.io/small-sitemap.xml"
    create_source = await CustomGPT.Source.acreate(project_id=project_id, sitemap_path=new_sitemap_path)
    data = create_source.parsed.data
    assert data.type == "sitemap"
    assert create_source.status_code == 201

    # Add File To Project
    with open(file_path, "rb") as file:
        file_content = file.read()

    create_source = await CustomGPT.Source.acreate(
        project_id=project_id, file=File(payload=file_content, file_name="vanka.pdf")
    )
    data = create_source.parsed.data
    assert create_source.status_code == 201
    assert data.type == "upload"

    # List Sources
    list_sources = await CustomGPT.Source.alist(project_id=project_id)
    data = list_sources.parsed.data
    assert list_sources.status_code == 200
    assert len(data.sitemaps) > 0

    # # Delete Source
    source_id = data.sitemaps[0].id
    delete_source = await CustomGPT.Source.adelete(project_id=project_id, source_id=source_id)
    assert delete_source.status_code == 200
