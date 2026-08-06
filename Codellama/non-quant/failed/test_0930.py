import pytest
from src_0930 import task_func

def test_task_func_empty_string():
    word = ""
    expected_result = np.array([])
    assert np.array_equal(task_func(word), expected_result)

def test_task_func_single_char():
    word = "a"
    expected_result = np.array([0])
    assert np.array_equal(task_func(word), expected_result)

def test_task_func_multiple_chars():
    word = "hello"
    expected_result = np.array([4, 1, 2, 2, 1])
    assert np.array_equal(task_func(word), expected_result)

def test_task_func_non_ascii_chars():
    word = "hello world"
    expected_result = np.array([4, 1, 2, 2, 1, 3, 1, 2, 2, 1])
    assert np.array_equal(task_func(word), expected_result)