import pytest
from src_0099 import task_func

def test_task_func():
    num_strings = 10
    string_length = 10
    expected_result = [('a', 10), ('b', 10), ('c', 10), ('d', 10), ('e', 10), ('f', 10), ('g', 10), ('h', 10), ('i', 10), ('j', 10)]
    assert task_func(num_strings, string_length) == expected_result

def test_task_func_with_different_num_strings():
    num_strings = 20
    string_length = 10
    expected_result = [('a', 20), ('b', 20), ('c', 20), ('d', 20), ('e', 20), ('f', 20), ('g', 20), ('h', 20), ('i', 20), ('j', 20)]
    assert task_func(num_strings, string_length) == expected_result

def test_task_func_with_different_string_length():
    num_strings = 10
    string_length = 20
    expected_result = [('a', 10), ('b', 10), ('c', 10), ('d', 10), ('e', 10), ('f', 10), ('g', 10), ('h', 10), ('i', 10), ('j', 10)]
    assert task_func(num_strings, string_length) == expected_result

def test_task_func_with_different_num_strings_and_string_length():
    num_strings = 20
    string_length = 20
    expected_result = [('a', 20), ('b', 20), ('c', 20), ('d', 20), ('e', 20), ('f', 20), ('g', 20), ('h', 20), ('i', 20), ('j', 20)]
    assert task_func(num_strings, string_length) == expected_result