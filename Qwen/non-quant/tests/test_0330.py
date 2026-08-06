import pytest
from src_0330 import task_func
import os
import json

# Mocking the file reading and JSON loading
def mock_open(data):
    class MockFile:
        def __init__(self, data):
            self.data = data

        def read(self):
            return json.dumps(self.data)

    return MockFile(data)

def test_task_func_with_default_pattern(monkeypatch):
    # Mock the open function to return mock data
    mock_data = {'key1': 'value1', 'key2': 'value2'}
    monkeypatch.setattr('builtins.open', lambda path, mode: mock_open(mock_data))
    
    # Call the function
    result = task_func('test_file.json')
    
    # Expected result based on the default regex pattern
    expected_result = {'test_file.json': ['value1', 'value2']}
    assert result == expected_result

def test_task_func_with_custom_pattern(monkeypatch):
    # Mock the open function to return mock data
    mock_data = {'key1': 'example (text)', 'key2': 'another example'}
    monkeypatch.setattr('builtins.open', lambda path, mode: mock_open(mock_data))
    
    # Define a custom regex pattern
    custom_pattern = r'\bexample\b'
    
    # Call the function with the custom pattern
    result = task_func('test_file.json', custom_pattern)
    
    # Expected result based on the custom regex pattern
    expected_result = {'test_file.json': ['example']}
    assert result == expected_result

def test_task_func_with_no_matches(monkeypatch):
    # Mock the open function to return mock data
    mock_data = {'key1': 'no match here', 'key2': 'also no match'}
    monkeypatch.setattr('builtins.open', lambda path, mode: mock_open(mock_data))
    
    # Call the function
    result = task_func('test_file.json')
    
    # Expected result when no matches are found
    expected_result = {'test_file.json': []}
    assert result == expected_result

def test_task_func_with_empty_file(monkeypatch):
    # Mock the open function to return mock data
    mock_data = {}
    monkeypatch.setattr('builtins.open', lambda path, mode: mock_open(mock_data))
    
    # Call the function
    result = task_func('test_file.json')
    
    # Expected result when the file is empty
    expected_result = {'test_file.json': []}
    assert result == expected_result