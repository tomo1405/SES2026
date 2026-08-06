import pytest
from src_1109 import task_func

def test_task_func():
    result = [
        {"url": "https://www.example.com", "name": "John Doe"},
        {"url": "https://www.example.com", "name": "Jane Doe"},
        {"url": "https://www.example.com", "name": "John Doe"},
        {"url": "https://www.example.com", "name": "Jane Doe"},
        {"url": "https://www.example.com", "name": "John Doe"},
    ]
    expected_result = {"https://www.example.com": 3}

    assert task_func(result) == expected_result