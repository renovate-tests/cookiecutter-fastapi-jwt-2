from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)

email = "bsmith@aol.com"
password = "sup3r$ecreT"


def signUp():
    client.post(
        "/user/signup",
        json={
            "fullname": "Bob Smith",
            "email": email,
            "password": password,
        },
    )


def test_signIn():
    # create the test account before trying to sign-in
    signUp()

    response = client.post(
        "/user/login",
        json={"email": email, "password": password},
    )
    assert response.status_code == 200
    assert "access_token" in response.json()

    return response.json()["access_token"]
