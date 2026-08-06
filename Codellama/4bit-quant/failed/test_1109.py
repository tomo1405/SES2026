import pytest
from src_1109 import task_func

def test_task_func():
    result = [
        {'url': 'https://www.example.com', 'name': 'John Doe'},
        {'url': 'https://www.example.com', 'name': 'Jane Doe'},
        {'url': 'https://www.example.com', 'name': 'John Doe'},
        {'url': 'https://www.example.com', 'name': 'Jane Doe'},
        {'url': 'https://www.example.com', 'name': 'John Doe'},
        {'url': 'https://www.example.com', 'name': 'Jane Doe'},
        {'url': 'https://www.example.com', 'name': 'John Doe'},
        {'url': 'https://www.example.com', 'name': 'Jane Doe'},
        {'url': 'https://www.example.com', 'name': 'John Doe'},
        {'url': 'https://www.example.com', 'name': 'Jane Doe'},
    ]
    expected_result = {'https://www.example.com': 10}
    assert task_func(result) == expected_result

def test_task_func_empty_input():
    result = []
    expected_result = {}
    assert task_func(result) == expected_result

def test_task_func_invalid_input():
    result = [
        {'url': 'https://www.example.com', 'name': 'John Doe'},
        {'url': 'https://www.example.com', 'name': 'Jane Doe'},
        {'url': 'https://www.example.com', 'name': 'John Doe'},
        {'url': 'https://www.example.com', 'name': 'Jane Doe'},
        {'url': 'https://www.example.com', 'name': 'John Doe'},
        {'url': 'https://www.example.com', 'name': 'Jane Doe'},
        {'url': 'https://www.example.com', 'name': 'John Doe'},
        {'url': 'https://www.example.com', 'name': 'Jane Doe'},
        {'url': 'https://www.example.com', 'name': 'John Doe'},
        {'url': 'https://www.example.com', 'name': 'Jane Doe'},
    ]
    expected_result = {'https://www.example.com': 10}
    assert task_func(result) == expected_result

def test_task_func_invalid_input_2():
    result = [
        {'url': 'https://www.example.com', 'name': 'John Doe'},
        {'url': 'https://www.example.com', 'name': 'Jane Doe'},
        {'url': 'https://www.example.com', 'name': 'John Doe'},
        {'url': 'https://www.example.com', 'name': 'Jane Doe'},
        {'url': 'https://www.example.com', 'name': 'John Doe'},
        {'url': 'https://www.example.com', 'name': 'Jane Doe'},
        {'url': 'https://www.example.com', 'name': 'John Doe'},
        {'url': 'https://www.example.com', 'name': 'Jane Doe'},
        {'url': 'https://www.example.com', 'name': 'John Doe'},
        {'url': 'https://www.example.com', 'name': 'Jane Doe'},
    ]
    expected_result = {'https://www.example.com': 10}
    assert task_func(result) == expected_result