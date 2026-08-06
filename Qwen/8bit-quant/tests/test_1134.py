import json
from unittest.mock import Mock, patch

import pytest
import requests
from src_1134 import task_func


@pytest.mark.parametrize("endpoint", ["/data", "/users", "/posts"])
def test_task_func_success(endpoint):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"key": "value"}
    
    with patch('requests.get', return_value=mock_response):
        result = task_func("http://example.com", endpoint, "prefix_")
        
        assert result == f"prefix_{endpoint}.json"
        with open(result, 'r') as f:
            data = json.load(f)
            assert data == {"key": "value"}

def test_task_func_failure():
    mock_response = Mock()
    mock_response.status_code = 500
    
    with patch('requests.get', return_value=mock_response), pytest.raises(RuntimeError) as excinfo:
        task_func("http://example.com", "/error", "prefix_")
        
        assert "Error fetching data from API" in str(excinfo.value)

def test_task_func_request_exception():
    with patch('requests.get', side_effect=requests.RequestException("Connection error")), pytest.raises(RuntimeError) as excinfo:
        task_func("http://example.com", "/error", "prefix_")
        
        assert "Error fetching data from API: Connection error" in str(excinfo.value)