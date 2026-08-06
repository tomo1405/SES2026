import pytest
from src_0033 import task_func

def test_task_func():
    url = "https://www.example.com"
    tag = "h1"
    expected_output = "Example Domain"
    
    response = task_func(url, tag)
    
    assert response == expected_output, "The function returned an incorrect output"

def test_task_func_with_invalid_tag():
    url = "https://www.example.com"
    tag = "invalid_tag"
    expected_output = None
    
    response = task_func(url, tag)
    
    assert response == expected_output, "The function returned an incorrect output"

def test_task_func_with_invalid_url():
    url = "https://invalid_url"
    tag = "h1"
    expected_output = None
    
    response = task_func(url, tag)
    
    assert response == expected_output, "The function returned an incorrect output"