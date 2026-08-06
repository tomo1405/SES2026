import pytest
from src_0318 import task_func

def test_task_func():
    example_str = '[This is a test string]'
    expected_result = {'This': 1.0, 'is': 1.0, 'a': 1.0, 'test': 1.0, 'string': 1.0}
    assert task_func(example_str) == expected_result

def test_task_func_empty_string():
    example_str = ''
    expected_result = {}
    assert task_func(example_str) == expected_result

def test_task_func_no_brackets():
    example_str = 'This is a test string'
    expected_result = {'This': 1.0, 'is': 1.0, 'a': 1.0, 'test': 1.0, 'string': 1.0}
    assert task_func(example_str) == expected_result

def test_task_func_multiple_brackets():
    example_str = '[This is a test string] [This is another test string]'
    expected_result = {'This': 2.0, 'is': 2.0, 'a': 2.0, 'test': 2.0, 'string': 2.0}
    assert task_func(example_str) == expected_result