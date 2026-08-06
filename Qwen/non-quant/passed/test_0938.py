import pytest
from src_0938 import task_func

def test_task_func_empty_string():
    assert task_func("") == {}

def test_task_func_only_spaces():
    assert task_func("   ") == {}

def test_task_func_no_alphanumeric():
    assert task_func("!@#$%^&*()") == {}

def test_task_func_single_character():
    assert task_func("a") == {'a': 1}

def test_task_func_multiple_characters():
    assert task_func("aabbcc") == {'a': 2, 'b': 2, 'c': 2}

def test_task_func_case_insensitivity():
    assert task_func("AaBbCc") == {'a': 2, 'b': 2, 'c': 2}

def test_task_func_with_punctuation():
    assert task_func("Hello, World!") == {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

def test_task_func_with_numbers():
    assert task_func("1234567890") == {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '0': 1}

def test_task_func_mixed_alphanumeric():
    assert task_func("a1b2c3") == {'a': 1, '1': 1, 'b': 1, '2': 1, 'c': 1, '3': 1}