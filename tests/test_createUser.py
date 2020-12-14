from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


email = "bsmith@aol.com"
password = "sup3r$ecreT"


def test_signUp():
    response = client.post(
        "/user/signup",
        json={
            "fullname": "Bob Smith",
            "email": email,
            "password": password,
        },
    )
    assert response.status_code == 201
    assert "access_token" in response.json()
