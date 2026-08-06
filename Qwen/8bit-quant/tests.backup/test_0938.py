import pytest
from src_0938 import task_func

def test_task_func_empty_string():
    assert task_func("") == Counter()

def test_task_func_no_special_characters():
    assert task_func("HelloWorld") == Counter({'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1})

def test_task_func_with_special_characters():
    assert task_func("Hello, World!") == Counter({'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1})

def test_task_func_case_insensitivity():
    assert task_func("Hello hello") == Counter({'h': 2, 'e': 2, 'l': 4, 'o': 2})

def test_task_func_numbers_included():
    assert task_func("123abcABC") == Counter({'a': 2, 'b': 2, 'c': 2, '1': 1, '2': 1, '3': 1})

def test_task_func_whitespace_only():
    assert task_func("   ") == Counter()

def test_task_func_punctuation_only():
    assert task_func("!@#$%^&*()") == Counter()