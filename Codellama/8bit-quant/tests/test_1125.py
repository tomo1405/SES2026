import pytest
from src_1125 import task_func

def test_task_func_valid_url():
    url = "https://www.example.com"
    result = task_func(url)
    assert result == "Example Domain"

def test_task_func_invalid_url():
    url = "https://www.example.com/invalid"
    result = task_func(url)
    assert result == "No valid URL found in the provided string."

def test_task_func_no_title():
    url = "https://www.example.com/no-title"
    result = task_func(url)
    assert result == "No title tag found in the webpage."

def test_task_func_invalid_domain():
    url = "https://www.example.com/invalid-domain"
    result = task_func(url)
    assert result == "Unable to fetch the content of the URL: https://www.example.com/invalid-domain"