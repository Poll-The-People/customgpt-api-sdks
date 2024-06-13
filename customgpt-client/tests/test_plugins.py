import json
import random
import string
import time

import pytest

from customgpt_client import CustomGPT
from tests.credentials import credentials


def test_sync_plugins():
    CustomGPT.base_url, CustomGPT.api_key = credentials()
    response = CustomGPT.Project.create(
        project_name="test",
        sitemap_path="https://adorosario.github.io/small-sitemap.xml",
    )
    response_project = response.parsed
    assert response.status_code == 201
    project_id = response_project.data.id
    json_project = {}
    is_chat_active = 0
    while not is_chat_active:
        response_project = CustomGPT.Project.get(project_id=project_id)
        json_project = response_project.parsed
        is_chat_active = json_project.data.is_chat_active
        time.sleep(5)

    plugin_name = "".join(random.choice(string.ascii_lowercase) for _ in range(10))

    # Add new sitemap to project using source api.
    create_plugin = CustomGPT.ProjectPlugins.create(
        project_id=project_id,
        model_name=plugin_name,
        human_name="The Indoor Plants",
        keywords="Indoor plants, Gardening, Trusted information.",
        description="Trusted information about indoor plants and gardening.",
        is_active=True,
    )
    model_name = create_plugin.parsed.data.model_name
    assert model_name == plugin_name
    assert create_plugin.status_code == 201

    # Update a plugin
    plugin_name2 = "".join(random.choice(string.ascii_lowercase) for _ in range(10))
    create_plugin = CustomGPT.ProjectPlugins.update(
        project_id=project_id,
        model_name=plugin_name2,
        human_name="The Indoor Plants",
        keywords="Indoor plants, Gardening, Trusted information.",
        description="Trusted information about indoor plants and gardening.",
        is_active=True,
    )
    model_name = create_plugin.parsed.data.model_name
    assert model_name == plugin_name2
    assert create_plugin.status_code == 200

    get_plugin = CustomGPT.ProjectPlugins.get(project_id=project_id)
    data = json.loads(get_plugin.content)["data"]
    assert get_plugin.status_code == 200
    assert data["model_name"] == plugin_name2


@pytest.mark.asyncio
async def test_async_plugins():
    CustomGPT.base_url, CustomGPT.api_key = credentials()
    response = await CustomGPT.Project.acreate(
        project_name="test",
        sitemap_path="https://adorosario.github.io/small-sitemap.xml",
    )
    response_project = response.parsed
    assert response.status_code == 201
    project_id = response_project.data.id
    json_project = {}
    is_chat_active = 0
    while not is_chat_active:
        response_project = await CustomGPT.Project.aget(project_id=project_id)
        json_project = response_project.parsed
        is_chat_active = json_project.data.is_chat_active
        time.sleep(5)

    plugin_name = "".join(random.choice(string.ascii_lowercase) for _ in range(10))

    # Add new sitemap to project using source api.
    create_plugin = await CustomGPT.ProjectPlugins.acreate(
        project_id=project_id,
        model_name=plugin_name,
        human_name="The Indoor Plants",
        keywords="Indoor plants, Gardening, Trusted information.",
        description="Trusted information about indoor plants and gardening.",
        is_active=True,
    )
    model_name = create_plugin.parsed.data.model_name
    assert model_name == plugin_name
    assert create_plugin.status_code == 201

    # Update a plugin
    plugin_name2 = "".join(random.choice(string.ascii_lowercase) for _ in range(10))
    create_plugin = await CustomGPT.ProjectPlugins.aupdate(
        project_id=project_id,
        model_name=plugin_name2,
        human_name="The Indoor Plants",
        keywords="Indoor plants, Gardening, Trusted information.",
        description="Trusted information about indoor plants and gardening.",
        is_active=True,
    )
    model_name = create_plugin.parsed.data.model_name
    assert model_name == plugin_name2
    assert create_plugin.status_code == 200

    get_plugin = await CustomGPT.ProjectPlugins.aget(project_id=project_id)
    data = json.loads(get_plugin.content)["data"]
    assert get_plugin.status_code == 200
    assert data["model_name"] == plugin_name2
