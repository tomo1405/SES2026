from unittest.mock import Mock, patch

import pytest
import requests
from PIL import Image
from src_1011 import task_func


def test_task_func_success():
    url = "http://example.com/image.jpg"
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.content = b"image_data"
    mock_response.raise_for_status = lambda: None

    with patch('requests.get', return_value=mock_response):
        image = task_func(url)
        assert isinstance(image, Image.Image)

def test_task_func_failure():
    url = "http://example.com/image.jpg"
    mock_response = Mock()
    mock_response.status_code = 404
    mock_response.raise_for_status = Mock(side_effect=requests.exceptions.HTTPError("HTTP Error"))

    with patch('requests.get', return_value=mock_response):
        with pytest.raises(ValueError) as excinfo:
            task_func(url)
        assert str(excinfo.value) == f"Failed to retrieve image from {url}: HTTP Error"

def test_task_func_timeout():
    url = "http://example.com/image.jpg"
    with patch('requests.get', side_effect=requests.exceptions.Timeout):
        with pytest.raises(ValueError) as excinfo:
            task_func(url)
        assert str(excinfo.value).startswith(f"Failed to retrieve image from {url}: ")

def test_task_func_invalid_image():
    url = "http://example.com/image.jpg"
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.content = b"invalid_image_data"
    mock_response.raise_for_status = lambda: None

    with patch('requests.get', return_value=mock_response):
        with pytest.raises(ValueError) as excinfo:
            task_func(url)
        assert str(excinfo.value).startswith(f"Failed to retrieve image from {url}: ")