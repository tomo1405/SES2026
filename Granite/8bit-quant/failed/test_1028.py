import pytest
from src_1028 import task_func

def test_task_func():
    url_with_query = "https://www.example.com/?q=42"
    expected_output = "42"
    assert task_func(url_with_query) == expected_output

    url_without_query = "https://www.example.com/"
    expected_output = None
    assert task_func(url_without_query) == expected_output

    invalid_url = "https://www.example.com/foo"
    expected_output = None
    assert task_func(invalid_url) == expected_output