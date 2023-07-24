import httpx
import pytest

@pytest.mark.asyncio
async def test_sign_new_user(default_client: httpx.AsyncClient) -> None:
    payload = {
        "email": "test@example.com",
        "password": "testpassword",
        "username": "test"
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }
    test_response = {
        "message": "User successfully registered"
    }
    response = await default_client.post("/user/signup",
                                         json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json() == test_response


@pytest.mark.asyncio
async def test_sign_user_in(default_client: httpx.AsyncClient) -> None:
    payload = {
        "username": "test@example.com",
        "password": "testpassword",
    }
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = await default_client.post("/user/signin",
                                         data=payload, headers=headers)
    assert response.status_code == 200
    assert response.json()["token_type"] == "Bearer"