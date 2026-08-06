import pytest
from src_0997 import task_func
import os
import requests
from unittest.mock import patch, MagicMock

def test_task_func_valid_url(tmp_path):
    # Arrange
    url = "http://example.com"
    file_name = tmp_path / "Output.txt"
    expected_title = "Example Domain"
    
    with patch('requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "<html><head><title>Example Domain</title></head><body></body></html>"
        mock_get.return_value = mock_response
        
        # Act
        result = task_func(url, str(file_name))
        
        # Assert
        assert result == str(file_name)
        assert file_name.exists()
        with open(file_name, "r", encoding="utf-8") as f:
            content = f.read().strip()
            assert content == '{"title": "Example Domain"}'

def test_task_func_invalid_url(tmp_path):
    # Arrange
    url = "http://invalid-url"
    file_name = tmp_path / "Output.txt"
    
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.exceptions.RequestException("Connection error")
        
        # Act & Assert
        with pytest.raises(requests.exceptions.RequestException) as excinfo:
            task_func(url, str(file_name))
        assert str(excinfo.value) == "Connection error"
        assert not file_name.exists()

def test_task_func_no_title(tmp_path):
    # Arrange
    url = "http://example.com"
    file_name = tmp_path / "Output.txt"
    
    with patch('requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "<html><head></head><body></body></html>"
        mock_get.return_value = mock_response
        
        # Act
        result = task_func(url, str(file_name))
        
        # Assert
        assert result == str(file_name)
        assert file_name.exists()
        with open(file_name, "r", encoding="utf-8") as f:
            content = f.read().strip()
            assert content == '{"title": null}'

def test_task_func_file_exists(tmp_path):
    # Arrange
    url = "http://example.com"
    file_name = tmp_path / "Output.txt"
    existing_content = '{"title": "Existing Title"}\n'
    file_name.write_text(existing_content)
    
    with patch('requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "<html><head><title>New Title</title></head><body></body></html>"
        mock_get.return_value = mock_response
        
        # Act
        result = task_func(url, str(file_name))
        
        # Assert
        assert result == str(file_name)
        assert file_name.exists()
        with open(file_name, "r", encoding="utf-8") as f:
            content = f.read().strip()
            assert content == existing_content.strip() + '\n{"title": "New Title"}'