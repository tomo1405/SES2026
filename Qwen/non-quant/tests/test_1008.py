import pytest
from src_1008 import task_func
import requests
import pandas as pd
from unittest.mock import patch, Mock

def test_task_func_success():
    url = "https://api.example.com/data"
    mock_data = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
    
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response
        
        df = task_func(url)
        
        assert isinstance(df, pd.DataFrame)
        assert df.equals(pd.DataFrame(mock_data))

def test_task_func_network_error():
    url = "https://api.example.com/data"
    
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.RequestException("Connection failed")
        mock_get.return_value = mock_response
        
        with pytest.raises(SystemError) as exc_info:
            task_func(url)
        
        assert "Network error occurred" in str(exc_info.value)

def test_task_func_invalid_json():
    url = "https://api.example.com/data"
    
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.side_effect = ValueError("Invalid JSON")
        mock_get.return_value = mock_response
        
        with pytest.raises(ValueError) as exc_info:
            task_func(url)
        
        assert "Invalid JSON format for DataFrame conversion" in str(exc_info.value)