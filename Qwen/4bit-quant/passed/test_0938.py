import pytest
from src_0938 import task_func

def test_task_func_with_empty_string():
    assert task_func("") == {}

def test_task_func_with_only_spaces():
    assert task_func("   ") == {}

def test_task_func_with_only_special_characters():
    assert task_func("!@#$%^&*()") == {}

def test_task_func_with_mixed_characters():
    assert task_func("Hello, World!") == {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

def test_task_func_with_numbers():
    assert task_func("1234567890") == {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '0': 1}

def test_task_func_with_case_insensitivity():
    assert task_func("AaBbCc") == {'a': 2, 'b': 2, 'c': 2}

def test_task_func_with_repeated_letters():
    assert task_func("aabbcc") == {'a': 2, 'b': 2, 'c': 2}