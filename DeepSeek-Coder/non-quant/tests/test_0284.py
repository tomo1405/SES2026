import pytest
from src_0284 import task_func

# Test cases for task_func

def test_task_func_basic():
    # Test with a simple JSON file
    result = task_func('./test_files/', 'name')
    assert result == {'Alice': 1, 'Bob': 1, 'Charlie': 1}

def test_task_func_empty():
    # Test with an empty JSON file
    result = task_func('./test_files_empty/', 'name')
    assert result == {}

def test_task_func_no_files():
    # Test with a directory that has no JSON files
    result = task_func('./no_json_files/', 'name')
    assert result == {}

def test_task_func_no_key():
    # Test with a JSON file that does not contain the key
    result = task_func('./test_files/', 'nonexistent_key')
    assert result == {}

def test_task_func_multiple_files():
    # Test with multiple JSON files
    result = task_func('./test_files/', 'name')
    assert result == {'Alice': 2, 'Bob': 2, 'Charlie': 2}