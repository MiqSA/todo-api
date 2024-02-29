from tests.src.routers import PAYLOAD_SIGNUP

def test_01_success_v1_signup(test_client):
    response = test_client.post("/v1/signup", json=PAYLOAD_SIGNUP)
    res = response.json()
    assert response.status_code == 200
    assert res["email"] == PAYLOAD_SIGNUP["email"]
    assert res["message"] == "Success!"

def test_02_error_v1_signup_user_already_exist(test_client):
    response = test_client.post("/v1/signup", json=PAYLOAD_SIGNUP)
    res = response.json()
    assert response.status_code == 400
    assert res["detail"] == "User already exist."

def test_03_error_v1_signup_unique_values(test_client):
    payload_new = PAYLOAD_SIGNUP.copy()
    payload_new["email"] = "another@gmail.com"
    response = test_client.post("/v1/signup", json=payload_new)
    res = response.json()
    assert response.status_code == 422
    assert res["detail"] == "This username is not available, try another!"
