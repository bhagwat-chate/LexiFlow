# tests/test_unit_cases.py

import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "Document Portal" in response.text
