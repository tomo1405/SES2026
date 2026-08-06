import pytest
from src_1119 import task_func
from unittest.mock import patch, mock_open
import os

def test_task_func_default_values():
    # Test with default values
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.text = "header1,header2\nvalue1,value2"
        
        with patch('builtins.open', mock_open()) as mock_file:
            result = task_func()
            
            mock_get.assert_called_once_with('https://example.com/data.csv')
            mock_file.assert_called_once_with('data.json', 'w')
            
            assert result == 'data.json'
            expected_json_data = [{'header1': 'value1', 'header2': 'value2'}]
            mock_file().write.assert_called_once_with(json.dumps(expected_json_data, indent=4))

def test_task_func_custom_values():
    # Test with custom values
    csv_url = 'https://test.com/custom.csv'
    json_file_path = 'custom_data.json'
    
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.text = "name,age\nAlice,30"
        
        with patch('builtins.open', mock_open()) as mock_file:
            result = task_func(csv_url, json_file_path)
            
            mock_get.assert_called_once_with(csv_url)
            mock_file.assert_called_once_with(json_file_path, 'w')
            
            assert result == json_file_path
            expected_json_data = [{'name': 'Alice', 'age': '30'}]
            mock_file().write.assert_called_once_with(json.dumps(expected_json_data, indent=4))

def test_task_func_file_creation():
    # Test if file is created
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.text = "id,name\n1,Bob"
        
        with patch('builtins.open', mock_open()) as mock_file:
            task_func()
            
            assert os.path.exists('data.json')
            os.remove('data.json')

def test_task_func_file_cleanup():
    # Test if temporary files are cleaned up
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.text = "id,name\n1,Bob"
        
        with patch('builtins.open', mock_open()) as mock_file:
            task_func()
            
            assert not os.path.exists('data.json')