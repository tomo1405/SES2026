import pytest
from src_0033 import task_func

def test_task_func():
    url = "https://www.example.com"
    tag = "h1"
    expected_output = "Example Domain"

    output = task_func(url, tag)

    assert output == expected_output