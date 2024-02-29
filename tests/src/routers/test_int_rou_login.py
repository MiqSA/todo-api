from tests.src.routers import PAYLOAD_SIGNUP, PAYLOAD_LOGIN

def setUp(test_client):
    response = test_client.post("/v1/signup", json=PAYLOAD_SIGNUP)
    res = response.json()
    assert response.status_code == 200
    assert res["email"] == PAYLOAD_SIGNUP["email"]
    assert res["message"] == "Success!"

def test_01_success_v1_login(test_client):
    setUp(test_client)
    response = test_client.post("/v1/login", json=PAYLOAD_LOGIN)
    res = response.json()
    assert response.status_code == 200
    assert 'access_token' in res.keys()
    assert 'refresh_token' in res.keys()

def test_02_error_v1_login_incorrect_password(test_client):
    new_payload = PAYLOAD_LOGIN.copy()
    new_payload["password"] = "123"
    response = test_client.post("/v1/login", json=new_payload)
    res = response.json()
    assert response.status_code == 400
    assert res['detail'] == 'Password incorrect!'
