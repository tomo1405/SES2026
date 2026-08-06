import pytest
from src_0099 import task_func

def test_task_func():
    num_strings = 10
    string_length = 10
    expected_result = [('a', 10), ('b', 10), ('c', 10), ('d', 10), ('e', 10), ('f', 10), ('g', 10), ('h', 10), ('i', 10), ('j', 10)]
    assert task_func(num_strings, string_length) == expected_result

def test_task_func_with_different_num_strings():
    num_strings = 5
    string_length = 10
    expected_result = [('a', 5), ('b', 5), ('c', 5), ('d', 5), ('e', 5), ('f', 5), ('g', 5), ('h', 5), ('i', 5), ('j', 5)]
    assert task_func(num_strings, string_length) == expected_result

def test_task_func_with_different_string_length():
    num_strings = 10
    string_length = 5
    expected_result = [('a', 10), ('b', 10), ('c', 10), ('d', 10), ('e', 10), ('f', 10), ('g', 10), ('h', 10), ('i', 10), ('j', 10)]
    assert task_func(num_strings, string_length) == expected_result