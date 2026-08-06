import pytest
from src_0767 import task_func

def test_task_func_type_error():
    with pytest.raises(TypeError):
        task_func(123)

def test_task_func_patterns_type_error():
    with pytest.raises(TypeError):
        task_func("abc", patterns=123)

def test_task_func_patterns_value_error():
    with pytest.raises(ValueError):
        task_func("abc", patterns=["abc", 123])

def test_task_func_return_type():
    assert isinstance(task_func("abc"), dict)

def test_task_func_return_value():
    assert task_func("abc") == {"abc": 1}

def test_task_func_return_value_with_multiple_patterns():
    assert task_func("abcabcabc") == {"abc": 3}

def test_task_func_return_value_with_multiple_patterns_and_string():
    assert task_func("abcabcabcabc") == {"abc": 4}

def test_task_func_return_value_with_multiple_patterns_and_string_and_case_insensitive():
    assert task_func("abcABCabc") == {"abc": 3, "ABC": 1}