from fastapi.testclient import TestClient
from main import app
import pytest
from unittest.mock import patch
import json

client = TestClient(app)

def test_get_words():
    response = client.get("/get_words/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    
def test_get_words_with_error():
    response = client.post("/get_words/")
    assert response.status_code == 405

@patch('db.session')
def test_delete_all_words(mock_session):
    response = client.delete("/delete_all_words/")
    assert response.status_code == 200
    assert response.text == '"delete all words"'