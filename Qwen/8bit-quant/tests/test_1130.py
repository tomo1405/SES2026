import pytest
from src_1130 import task_func
import os
import json
import requests
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_json_data():
    return '{"test_key": "http://example.com"}'

@pytest.fixture
def mock_response():
    response = MagicMock()
    response.status_code = 200
    response.content = b"Sample content"
    return response

@patch('src_1130.requests.get')
def test_task_func(mock_get, mock_json_data, mock_response):
    mock_get.return_value = mock_response
    save_dir = '/tmp'
    expected_filename = "test_key_*.txt"
    
    result = task_func(mock_json_data, 'test_key', save_dir)
    
    assert mock_get.called_once_with("http://example.com")
    assert os.path.exists(result)
    assert os.path.isfile(result)
    assert len(os.listdir(save_dir)) == 1
    assert os.path.basename(result).startswith("test_key_")
    assert os.path.basename(result).endswith(".txt")

    with open(result, 'rb') as f:
        content = f.read()
    assert content == b"Sample content"

    # Clean up
    os.remove(result)

def test_task_func_invalid_json():
    with pytest.raises(json.JSONDecodeError):
        task_func("{invalid_json", "test_key")

@patch('src_1130.requests.get')
def test_task_func_url_not_found(mock_get, mock_json_data):
    mock_get.return_value.status_code = 404
    with pytest.raises(requests.exceptions.RequestException):
        task_func(mock_json_data, 'test_key')

@patch('src_1130.requests.get')
def test_task_func_missing_key(mock_get, mock_json_data):
    mock_get.return_value = MagicMock(status_code=200)
    with pytest.raises(KeyError):
        task_func(mock_json_data, 'non_existent_key')