import pytest
from src_1130 import task_func
import os
import json
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_response():
    mock_response = MagicMock()
    mock_response.content = b"Mock content"
    return mock_response

@patch('src_1130.requests.get')
@patch('src_1130.datetime')
def test_task_func(mock_datetime, mock_requests_get, mock_response, tmpdir):
    # Arrange
    mock_datetime.now.return_value.strftime.return_value = "20231005123456789012"
    mock_requests_get.return_value = mock_response
    json_data = '{"url_key": "http://example.com"}'
    unknown_key = "url_key"
    save_dir = str(tmpdir)

    # Act
    result = task_func(json_data, unknown_key, save_dir)

    # Assert
    expected_filename = "url_key_20231005123456789012.txt"
    expected_file_path = os.path.join(save_dir, expected_filename)
    assert result == expected_file_path
    assert os.path.exists(expected_file_path)
    with open(expected_file_path, 'rb') as f:
        content = f.read()
    assert content == b"Mock content"

    mock_requests_get.assert_called_once_with("http://example.com")
    mock_datetime.now.assert_called_once()
    mock_datetime.now.return_value.strftime.assert_called_once_with("%Y%m%d%H%M%S%f")

def test_task_func_default_save_dir(mock_response, tmpdir):
    # Arrange
    json_data = '{"url_key": "http://example.com"}'
    unknown_key = "url_key"
    save_dir = None

    # Act
    result = task_func(json_data, unknown_key, save_dir)

    # Assert
    expected_filename = "url_key_*.txt"
    expected_file_path = os.path.join(os.getcwd(), expected_filename)
    assert os.path.exists(result)
    assert expected_file_path.startswith(os.getcwd())
    with open(result, 'rb') as f:
        content = f.read()
    assert content == b"Mock content"