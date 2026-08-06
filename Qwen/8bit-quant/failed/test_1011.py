import pytest
from src_1011 import task_func
from PIL import Image
import io
import requests
from requests.exceptions import HTTPError, Timeout

def test_task_func_valid_url(mocker):
    # Mock the requests.get call to simulate a successful response
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.content = b'GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x21\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;'
    mock_response.raise_for_status = lambda: None
    mocker.patch('requests.get', return_value=mock_response)

    # Call the function with a valid URL
    image = task_func('http://example.com/image.gif')

    # Assert that the returned object is an instance of Image.Image
    assert isinstance(image, Image.Image)

def test_task_func_invalid_url(mocker):
    # Mock the requests.get call to simulate an invalid response
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    mock_response.raise_for_status = mocker.Mock(side_effect=HTTPError('404 Client Error: Not Found for url: http://example.com/image.gif'))
    mocker.patch('requests.get', return_value=mock_response)

    # Call the function with an invalid URL and expect a ValueError
    with pytest.raises(ValueError, match=r"Failed to retrieve image from http://example.com/image.gif: 404 Client Error: Not Found for url: http://example.com/image.gif"):
        task_func('http://example.com/image.gif')

def test_task_func_timeout(mocker):
    # Mock the requests.get call to simulate a timeout
    mocker.patch('requests.get', side_effect=Timeout('The request timed out'))

    # Call the function with a URL that causes a timeout and expect a ValueError
    with pytest.raises(ValueError, match=r"Failed to retrieve image from .*: The request timed out"):
        task_func('http://example.com/image.gif')

def test_task_func_other_exception(mocker):
    # Mock the requests.get call to simulate another exception
    mocker.patch('requests.get', side_effect=Exception('An unexpected error occurred'))

    # Call the function with a URL that causes an unexpected exception and expect a ValueError
    with pytest.raises(ValueError, match=r"Failed to retrieve image from .*: An unexpected error occurred"):
        task_func('http://example.com/image.gif')