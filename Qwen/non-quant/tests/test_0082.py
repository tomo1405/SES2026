import pytest
from flask import Flask
from flask_restful import Api
import requests
from unittest.mock import patch, Mock
from src_0082 import task_func

@pytest.fixture
def app():
    api_url = "http://example.com/api"
    template_folder = "/path/to/templates"
    return task_func(api_url, template_folder)

@pytest.fixture
def client(app):
    return app.test_client()

def test_task_func_returns_flask_app(app):
    assert isinstance(app, Flask)

def test_task_func_adds_resource(app):
    with app.test_request_context():
        assert 'DataResource' in app.view_functions

@patch('requests.get')
def test_data_resource_get(mock_get, client):
    mock_response = Mock()
    mock_response.json.return_value = {"key": "value"}
    mock_get.return_value = mock_response

    response = client.get('/data')
    
    assert response.status_code == 200
    assert response.json == {"key": "value"}
    mock_get.assert_called_once_with("http://example.com/api")