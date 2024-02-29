def test_0_success_health(test_client):
    response = test_client.get("/v1/health")
    assert response.status_code == 200
    res = response.json()
