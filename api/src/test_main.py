from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_user_list():
    response = client.get("/test_users")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_user():
    user_id = 1
    response = client.get(f"/test_users/{user_id}")
    assert response.status_code == 200
    assert response.json()  
    
def test_get_user_not_found():
    non_existing_user_id = 999
    response = client.get(f"/test_users/{non_existing_user_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}