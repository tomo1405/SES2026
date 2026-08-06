import pytest
from src_0029 import task_func
import requests
from unittest.mock import patch

def test_task_func_success():
    # Arrange
    data = {"key": "value"}
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = b'{"status": "success"}'
    
    with patch('requests.post') as mock_post:
        mock_post.return_value = mock_response
        # Act
        response = task_func(data)
        # Assert
        assert response.status_code == 200
        assert response.json() == {"status": "success"}

def test_task_func_failure():
    # Arrange
    data = {"key": "value"}
    mock_response = requests.Response()
    mock_response.status_code = 500
    mock_response._content = b'{"status": "error"}'
    
    with patch('requests.post') as mock_post:
        mock_post.return_value = mock_response
        # Act
        response = task_func(data)
        # Assert
        assert response.status_code == 500
        assert response.json() == {"status": "error"}

def test_task_func_with_custom_url():
    # Arrange
    data = {"key": "value"}
    custom_url = "http://custom-api-url.com"
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = b'{"status": "success"}'
    
    with patch('requests.post') as mock_post:
        mock_post.return_value = mock_response
        # Act
        response = task_func(data, url=custom_url)
        # Assert
        mock_post.assert_called_once_with(custom_url, json={"payload": "eyJrZXkiOiAidmFsdWUifQ=="})
        assert response.status_code == 200
        assert response.json() == {"status": "success"}