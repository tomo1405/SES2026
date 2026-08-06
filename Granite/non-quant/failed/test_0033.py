import pytest
from src_0033 import task_func

def test_task_func():
    url = 'https://www.example.com'
    tag = 'h1'
    expected_output = 'Example Domain'
    
    actual_output = task_func(url, tag)
    
    assert actual_output == expected_output, "Output does not match the expected output"

def test_task_func_with_invalid_url():
    url = 'https://www.invalidurl.com'
    tag = 'h1'
    expected_output = None
    
    actual_output = task_func(url, tag)
    
    assert actual_output == expected_output, "Output does not match the expected output"

def test_task_func_with_invalid_tag():
    url = 'https://www.example.com'
    tag = 'invalid_tag'
    expected_output = None
    
    actual_output = task_func(url, tag)
    
    assert actual_output == expected_output, "Output does not match the expected output"