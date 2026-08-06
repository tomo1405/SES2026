import pytest
import requests
from src_1125 import task_func


def test_no_url_found():
    assert task_func("This is a test string without a URL.") == "No valid URL found in the provided string."

def test_invalid_url():
    assert task_func("http://invalid-url") == "Unable to fetch the content of the URL: http://invalid-url"

def test_valid_url_no_title():
    with pytest.raises(requests.RequestException):
        # Mocking the requests.get call to raise an exception
        task_func("http://example.com")

def test_valid_url_with_title(mocker):
    # Mocking the requests.get call to return a response with a title
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = "<html><head><title>Test Title</title></head><body></body></html>"
    
    mocker.patch('requests.get', return_value=mock_response)
    
    assert task_func("http://example.com") == "Test Title"

def test_valid_url_without_title(mocker):
    # Mocking the requests.get call to return a response without a title
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = "<html><head></head><body></body></html>"
    
    mocker.patch('requests.get', return_value=mock_response)
    
    assert task_func("http://example.com") == "No title tag found in the webpage."