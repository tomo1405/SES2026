from unittest.mock import Mock, patch

import pytest
import requests
from src_1126 import task_func


def test_task_func():
    myString = "https://www.example.com"
    token = "abc123"
    expected_result = {"key": "value"}

    with pytest.raises(requests.exceptions.RequestException):
        task_func(myString, token)

    response_mock = Mock()
    response_mock.json.return_value = expected_result
    response_mock.status_code = 200

    with patch('requests.post', return_value=response_mock) as mock_post:
        result = task_func(myString, token)
        assert result == expected_result
        mock_post.assert_called_once_with('https://api.example.com/urls', headers={'Authorization': 'Bearer abc123'}, data='{"url": "https://www.example.com"}')