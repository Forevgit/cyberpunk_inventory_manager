import pytest
from httpx import AsyncClient, ASGITransport
from main import app

@pytest.mark.asyncio
async def test_create_item(authenticated_client):
    payload = {"name": "1newitem", "description": "Test item", "category": "Test", "quantity": 10, "price": 100.0}
    response = await authenticated_client.post("/inventory/", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "1newitem"

@pytest.mark.asyncio
async def test_read_items(authenticated_client):
    response = await authenticated_client.get("/inventory/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_read_item(authenticated_client):
    response = await authenticated_client.get("/inventory/1")
    assert response.status_code == 200
    assert "name" in response.json()

@pytest.mark.asyncio
async def test_update_item(authenticated_client):
    update_data = {"name": "Updated Item", "description": "Updated description"}
    response = await authenticated_client.put("/inventory/1", json=update_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Item"

@pytest.mark.asyncio
async def test_delete_item(authenticated_client):
    response = await authenticated_client.delete("/inventory/1")
    assert response.status_code == 200