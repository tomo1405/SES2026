import pytest
from src_0033 import task_func

def test_task_func():
    url = "https://www.example.com"
    tag = "h1"
    expected_output = "Example Domain"
    
    result = task_func(url, tag)
    
    assert result == expected_output, "The function did not return the expected output"

def test_task_func_with_invalid_tag():
    url = "https://www.example.com"
    tag = "invalid_tag"
    expected_output = None
    
    result = task_func(url, tag)
    
    assert result == expected_output, "The function did not return the expected output"