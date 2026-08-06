import pytest
from src_1021 import task_func
import requests
import chardet
import json

# Mocking the requests module
class MockResponse:
    def __init__(self, content, status_code=200):
        self.content = content
        self.status_code = status_code

    def json(self):
        return json.loads(self.content)

def test_task_func_default_parameters(mocker):
    # Mock the requests.get call
    mock_response_content = b'{"key": "value"}'
    mock_response = MockResponse(mock_response_content)
    mocker.patch('requests.get', return_value=mock_response)

    # Mock the chardet.detect call
    mocker.patch('chardet.detect', return_value={"encoding": "utf-8"})

    result = task_func()
    assert result == {"key": "value"}

def test_task_func_with_custom_url(mocker):
    custom_url = "http://custom-api.example.com/data"
    mock_response_content = b'{"key": "value"}'
    mock_response = MockResponse(mock_response_content)
    mocker.patch('requests.get', return_value=mock_response)

    # Mock the chardet.detect call
    mocker.patch('chardet.detect', return_value={"encoding": "utf-8"})

    result = task_func(custom_url)
    assert result == {"key": "value"}

def test_task_func_with_from_encoding(mocker):
    mock_response_content = b'{"key": "value"}'
    mock_response = MockResponse(mock_response_content)
    mocker.patch('requests.get', return_value=mock_response)

    result = task_func(from_encoding="utf-8")
    assert result == {"key": "value"}

def test_task_func_with_empty_content(mocker):
    mock_response_content = b''
    mock_response = MockResponse(mock_response_content)
    mocker.patch('requests.get', return_value=mock_response)

    result = task_func()
    assert result == {}

def test_task_func_with_detected_encoding_none(mocker):
    mock_response_content = b'{"key": "value"}'
    mock_response = MockResponse(mock_response_content)
    mocker.patch('requests.get', return_value=mock_response)

    # Mock the chardet.detect call to return None
    mocker.patch('chardet.detect', return_value={"encoding": None})

    with pytest.raises(ValueError, match="Unable to detect encoding for non-empty content"):
        task_func()

def test_task_func_with_non_json_response(mocker):
    mock_response_content = b'Not JSON content'
    mock_response = MockResponse(mock_response_content)
    mocker.patch('requests.get', return_value=mock_response)

    # Mock the chardet.detect call
    mocker.patch('chardet.detect', return_value={"encoding": "utf-8"})

    with pytest.raises(json.JSONDecodeError):
        task_func()