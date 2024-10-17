import pytest
import asyncio
from httpx import AsyncClient
from main import app

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture
async def authenticated_client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # registration_response = await ac.post(
        #     "/auth/register",
        #     json={"username": "sassa", "email": "example@example.com", "password": "password123"}
        # )

        # if registration_response.status_code == 400:
        login_response = await ac.post(
                "/auth/login",
                json={"username": "sassa", "password": "password123"}
            )
        # else:
        #     login_response = registration_response

        access_token = login_response.json()["access_token"]

        ac.headers = {"Authorization": f"Bearer {access_token}"}

        yield ac
