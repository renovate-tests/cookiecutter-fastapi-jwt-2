from fastapi.testclient import TestClient

from app.main import app
from .test_signIn import test_signIn


client = TestClient(app)


def test_createPost():
    # get the access token from the signIn test
    access_token = test_signIn()

    response = client.post(
        "/posts",
        # send the access_token in the "Authorization" header
        headers={"Authorization": "Bearer " + access_token},
        json={
            "title": "My post title",
            "content": "This is an example content section.",
        },
    )

    assert response.status_code == 201
