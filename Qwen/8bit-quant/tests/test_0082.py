import pytest
from src_0082 import task_func
from flask import Flask, jsonify
from unittest.mock import patch, MagicMock

@pytest.fixture
def client():
    app = Flask(__name__)
    api_url = "http://example.com/api/data"
    template_folder = "templates"
    app = task_func(api_url, template_folder)
    with app.test_client() as client:
        yield client

def test_data_resource_get(client):
    with patch('requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = {"key": "value"}
        mock_get.return_value = mock_response

        response = client.get('/data')
        assert response.status_code == 200
        assert response.json == {"key": "value"}

def test_data_resource_get_failure(client):
    with patch('requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = requests.exceptions.RequestException("Error")
        mock_get.return_value = mock_response

        response = client.get('/data')
        assert response.status_code == 500