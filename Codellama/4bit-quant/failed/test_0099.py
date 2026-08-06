import pytest
from src_0099 import task_func

def test_task_func():
    num_strings = 10
    string_length = 10
    expected_result = [('a', 10), ('b', 10), ('c', 10), ('d', 10), ('e', 10)]
    assert task_func(num_strings, string_length) == expected_result

def test_task_func_with_different_num_strings():
    num_strings = 5
    string_length = 10
    expected_result = [('a', 5), ('b', 5), ('c', 5), ('d', 5), ('e', 5)]
    assert task_func(num_strings, string_length) == expected_result

def test_task_func_with_different_string_length():
    num_strings = 10
    string_length = 5
    expected_result = [('a', 10), ('b', 10), ('c', 10), ('d', 10), ('e', 10)]
    assert task_func(num_strings, string_length) == expected_result

def test_task_func_with_invalid_input():
    num_strings = 0
    string_length = 0
    expected_result = []
    assert task_func(num_strings, string_length) == expected_result

if __name__ == '__main__':
    pytest.main()