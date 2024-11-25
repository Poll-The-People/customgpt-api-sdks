import pytest

from customgpt_client import CustomGPT
from tests.credentials import credentials


def test_sync_limits():
    CustomGPT.base_url, CustomGPT.api_key = credentials()
    CustomGPT.timeout = 10000
    response = CustomGPT.Limit.get()
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_async_limits():
    CustomGPT.base_url, CustomGPT.api_key = credentials()
    CustomGPT.timeout = 10000
    response = await CustomGPT.Limit.aget()
    assert response.status_code == 200

