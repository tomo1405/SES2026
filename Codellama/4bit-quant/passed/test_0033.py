import pytest
from src_0033 import task_func

def test_task_func():
    url = "https://www.example.com"
    tag = "h1"
    expected_result = "Example Domain"

    result = task_func(url, tag)

    assert result == expected_result