import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    # Since it redirects to /static/index.html, but TestClient follows redirects by default
    # Actually, the root redirects to /static/index.html, so it should return the HTML content
    assert "text/html" in response.headers["content-type"]

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert "Debate Club" in data
    assert isinstance(data, dict)