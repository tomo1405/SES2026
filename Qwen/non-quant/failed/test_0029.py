import pytest
from src_0029 import task_func
import requests
import json
import base64

# Mocking the requests.post function to avoid actual HTTP calls
class MockResponse:
    def __init__(self, status_code, text):
        self.status_code = status_code
        self.text = text

    def json(self):
        return json.loads(self.text)

def mock_post(*args, **kwargs):
    # Simulate a successful response
    return MockResponse(200, '{"status": "success"}')

def test_task_func_success(mocker):
    # Arrange
    data = {"key": "value"}
    url = "http://your-api-url.com"
    expected_json_data = json.dumps(data)
    expected_encoded_data = base64.b64encode(expected_json_data.encode('ascii')).decode('ascii')
    expected_payload = {"payload": expected_encoded_data}

    # Mock the requests.post call
    mocker.patch('requests.post', side_effect=mock_post)

    # Act
    response = task_func(data, url)

    # Assert
    requests.post.assert_called_once_with(url, json=expected_payload)
    assert response.status_code == 200
    assert response.json() == {"status": "success"}

def test_task_func_failure(mocker):
    # Arrange
    data = {"key": "value"}
    url = "http://your-api-url.com"
    expected_json_data = json.dumps(data)
    expected_encoded_data = base64.b64encode(expected_json_data.encode('ascii')).decode('ascii')
    expected_payload = {"payload": expected_encoded_data}

    # Mock the requests.post call to simulate a failure
    mocker.patch('requests.post', side_effect=MockResponse(500, '{"status": "error"}'))

    # Act
    response = task_func(data, url)

    # Assert
    requests.post.assert_called_once_with(url, json=expected_payload)
    assert response.status_code == 500
    assert response.json() == {"status": "error"}