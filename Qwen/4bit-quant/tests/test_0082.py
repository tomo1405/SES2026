import pytest
from flask import Flask
from flask_restful import Api
import requests
from src_0082 import task_func

# Mocking the requests.get function to simulate API responses
class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

def mock_requests_get(*args, **kwargs):
    if args[0] == 'http://example.com/api/data':
        return MockResponse({"key": "value"}, 200)
    return MockResponse(None, 404)

@pytest.fixture
def client():
    app = task_func('http://example.com/api/data', 'templates')
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def mock_requests(monkeypatch):
    monkeypatch.setattr(requests, 'get', mock_requests_get)

def test_data_resource(client):
    response = client.get('/data')
    assert response.status_code == 200
    assert response.json == {"key": "value"}

def test_data_resource_not_found(client):
    response = client.get('/data/invalid')
    assert response.status_code == 404