import pytest
from src_1126 import task_func
import re
import json
import requests
from unittest.mock import patch, Mock

# Mocking the requests.post function to avoid actual HTTP requests during testing
@patch('src_1126.requests.post')
def test_task_func(mock_post):
    # Arrange
    myString = "Check out this link: https://example.com"
    token = "mock_token"
    expected_url = "https://example.com"
    mock_response = Mock()
    mock_response.json.return_value = {"status": "success", "url": expected_url}
    mock_post.return_value = mock_response

    # Act
    result = task_func(myString, token)

    # Assert
    assert result == {"status": "success", "url": expected_url}
    mock_post.assert_called_once_with(
        'https://api.example.com/urls',
        headers={'Authorization': 'Bearer mock_token'},
        data=json.dumps({'url': expected_url})
    )

def test_task_func_invalid_string():
    # Arrange
    myString = "No URL here"
    token = "mock_token"

    # Act & Assert
    with pytest.raises(AttributeError):
        task_func(myString, token)