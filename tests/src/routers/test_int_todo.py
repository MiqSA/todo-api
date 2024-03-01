from tests.src.routers import PAYLOAD_SIGNUP, PAYLOAD_LOGIN
from unittest.mock import patch


def setUp(test_client):
    response = test_client.post("/v1/signup", json=PAYLOAD_SIGNUP)
    res = response.json()
    assert response.status_code == 200
    assert res["message"] == "Success!"

    response = test_client.post("/v1/login", json=PAYLOAD_LOGIN)
    res = response.json()
    assert response.status_code == 200
    assert 'access_token' in res.keys()
    return res["access_token"]


def test_0_success_todo_default(test_client):
    access_token = setUp(test_client)
    headers = {"Authorization": f"Bearer {access_token}"}
    response = test_client.get("/v1/todo", headers=headers)
    res = response.json()
    assert response.status_code == 200
    assert len(res) == 5

def test_1_error_todo_unauthorized(test_client):
    response = test_client.get("/v1/todo")
    assert response.status_code == 403
    res = response.json()
    assert res == {'detail': 'Not authenticated'} 
