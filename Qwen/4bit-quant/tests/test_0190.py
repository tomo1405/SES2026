import requests
from src_0190 import task_func


def test_task_func_valid_url():
    # Mocking the requests.get call to simulate a valid response
    def mock_get(url):
        class MockResponse:
            def __init__(self, data):
                self.data = data
            
            def json(self):
                return self.data
        
        return MockResponse({'names': ['Alice', 'Bob', 'Charlie']})
    
    requests.get = mock_get
    
    result = task_func('http://example.com/data')
    assert result == ['Alice', 'Bob', 'Charlie']

def test_task_func_invalid_url():
    # Mocking the requests.get call to simulate an invalid response
    def mock_get(url):
        raise requests.exceptions.RequestException("Invalid URL")
    
    requests.get = mock_get
    
    result = task_func('http://invalid-url')
    assert result == "Invalid url input"

def test_task_func_no_names_key():
    # Mocking the requests.get call to simulate a response without 'names' key
    def mock_get(url):
        class MockResponse:
            def __init__(self, data):
                self.data = data
            
            def json(self):
                return self.data
        
        return MockResponse({'other_key': ['Alice', 'Bob', 'Charlie']})
    
    requests.get = mock_get
    
    result = task_func('http://example.com/data')
    assert result == []

def test_task_func_empty_names_list():
    # Mocking the requests.get call to simulate an empty 'names' list
    def mock_get(url):
        class MockResponse:
            def __init__(self, data):
                self.data = data
            
            def json(self):
                return self.data
        
        return MockResponse({'names': []})
    
    requests.get = mock_get
    
    result = task_func('http://example.com/data')
    assert result == []