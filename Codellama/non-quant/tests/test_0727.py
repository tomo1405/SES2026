import pytest
from src_0727 import task_func

def test_task_func_with_valid_input():
    s = "The quick brown fox jumps over the lazy dog"
    n = 3
    expected_output = ["the", "quick", "brown"]
    assert task_func(s, n) == expected_output

def test_task_func_with_invalid_input():
    s = "The quick brown fox jumps over the lazy dog"
    n = 100
    expected_output = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    assert task_func(s, n) == expected_output

def test_task_func_with_empty_string():
    s = ""
    n = 3
    expected_output = []
    assert task_func(s, n) == expected_output

def test_task_func_with_invalid_n():
    s = "The quick brown fox jumps over the lazy dog"
    n = -1
    expected_output = []
    assert task_func(s, n) == expected_output

def test_task_func_with_invalid_n_and_empty_string():
    s = ""
    n = -1
    expected_output = []
    assert task_func(s, n) == expected_output