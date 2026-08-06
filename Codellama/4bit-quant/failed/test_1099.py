import pytest
from src_1099 import task_func

def test_task_func():
    text = "This is a sample text for testing the task function."
    top_n = 3
    expected_result = [('sample', 2), ('testing', 1), ('task', 1)]
    assert task_func(text, top_n) == expected_result

def test_task_func_with_empty_text():
    text = ""
    top_n = 3
    expected_result = []
    assert task_func(text, top_n) == expected_result

def test_task_func_with_top_n_greater_than_number_of_words():
    text = "This is a sample text for testing the task function."
    top_n = 10
    expected_result = [('sample', 2), ('testing', 1), ('task', 1)]
    assert task_func(text, top_n) == expected_result

def test_task_func_with_top_n_less_than_number_of_words():
    text = "This is a sample text for testing the task function."
    top_n = 2
    expected_result = [('sample', 2), ('testing', 1)]
    assert task_func(text, top_n) == expected_result