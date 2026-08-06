import pytest
from src_0767 import task_func

def test_task_func_basic():
    assert task_func("aabbcc", ['a', 'b', 'c']) == {'a': 2, 'b': 2, 'c': 2}

def test_task_func_invalid_input():
    with pytest.raises(TypeError):
        task_func(123)

def test_task_func_invalid_patterns():
    with pytest.raises(TypeError):
        task_func("test", "invalid_patterns")

def test_task_func_empty_string():
    assert task_func("", ['a', 'b', 'c']) == {'a': 0, 'b': 0, 'c': 0}

def test_task_func_no_matches():
    assert task_func("abc", ['x', 'y', 'z']) == {'x': 0, 'y': 0, 'z': 0}

def test_task_func_case_sensitive():
    assert task_func("AaAaA", ['a', 'A']) == {'a': 3, 'A': 3}

def test_task_func_large_input():
    string = "a" * 100000
    patterns = ['a']
    assert task_func(string, patterns=patterns) == {'a': 100000}