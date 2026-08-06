from unittest.mock import Mock, patch

import requests
from src_1125 import task_func


def test_task_func_no_url():
    result = task_func("This is a test string without a URL.")
    assert result == "No valid URL found in the provided string."

@patch('src_1125.requests.get')
def test_task_func_invalid_url(mock_get):
    mock_get.side_effect = requests.RequestException()
    result = task_func("https://invalid-url.com")
    assert result == "Unable to fetch the content of the URL: https://invalid-url.com"

@patch('src_1125.requests.get')
def test_task_func_no_title_tag(mock_get):
    mock_response = Mock()
    mock_response.text = "<html><body></body></html>"
    mock_get.return_value = mock_response
    result = task_func("https://example.com")
    assert result == "No title tag found in the webpage."

@patch('src_1125.requests.get')
def test_task_func_valid_url_with_title(mock_get):
    mock_response = Mock()
    mock_response.text = "<html><head><title>Test Title</title></head><body></body></html>"
    mock_get.return_value = mock_response
    result = task_func("https://example.com")
    assert result == "Test Title"