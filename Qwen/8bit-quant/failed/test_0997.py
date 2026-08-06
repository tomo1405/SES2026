import pytest
from src_0997 import task_func
from unittest.mock import patch, mock_open
import os

@pytest.fixture
def mock_response():
    class MockResponse:
        def __init__(self, text):
            self.text = text

    return MockResponse('<html><head><title>Test Title</title></head><body></body></html>')

@patch('requests.get')
@patch('builtins.open', new_callable=mock_open)
def test_task_func(mock_open, mock_get, mock_response):
    mock_get.return_value = mock_response
    url = "http://example.com"
    file_name = "test_output.txt"
    
    result = task_func(url, file_name)
    
    assert result == file_name
    
    mock_get.assert_called_once_with(url, timeout=5)
    mock_open.assert_called_once_with(file_name, "a", encoding="utf-8")
    handle = mock_open()
    handle().write.assert_called_once_with('{"title": "Test Title"}\n')

def test_task_func_no_title(mock_response):
    class MockResponseNoTitle:
        def __init__(self, text):
            self.text = text

    mock_response_no_title = MockResponseNoTitle('<html><head></head><body></body></html>')
    
    with patch('requests.get', return_value=mock_response_no_title), \
         patch('builtins.open', new_callable=mock_open) as mock_open:
        
        url = "http://example.com"
        file_name = "test_output.txt"
        
        result = task_func(url, file_name)
        
        assert result == file_name
        
        mock_open.assert_called_once_with(file_name, "a", encoding="utf-8")
        handle = mock_open()
        handle().write.assert_called_once_with('{"title": null}\n')

def test_task_func_file_creation():
    url = "http://example.com"
    file_name = "test_output.txt"
    
    try:
        os.remove(file_name)
    except FileNotFoundError:
        pass
    
    task_func(url, file_name)
    
    assert os.path.exists(file_name)
    
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
    
    assert '{"title": null}' in content
    
    os.remove(file_name)