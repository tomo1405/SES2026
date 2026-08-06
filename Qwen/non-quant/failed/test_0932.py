import pytest
from src_0932 import task_func

def test_task_func_empty_string():
    result = task_func("")
    assert result == {}

def test_task_func_single_character():
    result = task_func("a")
    assert result == {}

def test_task_func_no_pairs():
    result = task_func("abc")
    assert result == {'ab': 1, 'bc': 1}

def test_task_func_with_repeated_characters():
    result = task_func("aabbcc")
    assert result == {'aa': 1, 'ab': 1, 'bb': 1, 'bc': 1, 'cc': 1}

def test_task_func_with_non_alphabetic_characters():
    result = task_func("a1b!c2d@")
    assert result == {'ab': 1, 'bc': 1, 'cd': 1}

def test_task_func_case_insensitivity():
    result = task_func("AbCdEfG")
    assert result == {'ab': 1, 'bc': 1, 'cd': 1, 'de': 1, 'ef': 1, 'fg': 1}