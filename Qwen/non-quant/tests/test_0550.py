import pytest
from src_0550 import task_func

def test_task_func_with_empty_dict():
    input_data = {}
    expected_output = "eJwBAA=="
    assert task_func(input_data) == expected_output

def test_task_func_with_single_row():
    input_data = {'A': [1], 'B': [2]}
    expected_output = "eJyrVspLzE1VslJSUdBKTrZSSklNzkxOS0vPSUzOTMxOS8uPyk1NzcvPz0="
    assert task_func(input_data) == expected_output

def test_task_func_with_multiple_rows():
    input_data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    expected_output = "eJyrVspLzE1VslJSUdBKTrZSSklNzkxOS0vPSUzOTMxOS8uPyk1NzcvPz0="
    assert task_func(input_data) == expected_output

def test_task_func_with_different_data_types():
    input_data = {'A': [1, 'two', 3.0], 'B': [True, False, None]}
    expected_output = "eJyrVspLzE1VslJSUdBKTrZSSklNzkxOS0vPSUzOTMxOS8uPyk1NzcvPz0="
    assert task_func(input_data) == expected_output

def test_task_func_with_special_characters():
    input_data = {'A': ['@', '#', '$'], 'B': ['%', '^', '&']}
    expected_output = "eJyrVspLzE1VslJSUdBKTrZSSklNzkxOS0vPSUzOTMxOS8uPyk1NzcvPz0="
    assert task_func(input_data) == expected_output