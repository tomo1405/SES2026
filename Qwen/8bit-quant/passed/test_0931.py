import pytest
from src_0931 import task_func

def test_task_func_input_validation():
    with pytest.raises(ValueError):
        task_func("123")
    with pytest.raises(ValueError):
        task_func("!@#")
    with pytest.raises(ValueError):
        task_func("abc123")

def test_task_func_short_word():
    result = task_func("a")
    assert result == ['', '', '']

def test_task_func_single_letter():
    result = task_func("a")
    assert result == ['', '', '']

def test_task_func_two_letters():
    result = task_func("ab")
    assert len(result) == 3
    assert all(isinstance(item, str) for item in result)

def test_task_func_long_word():
    result = task_func("abcdefg")
    assert len(result) == 3
    assert all(isinstance(item, str) for item in result)

def test_task_func_repeated_letters():
    result = task_func("aaaa")
    assert len(result) == 3
    assert all(isinstance(item, str) for item in result)

def test_task_func_mixed_case():
    result = task_func("AbCdEfG")
    assert len(result) == 3
    assert all(isinstance(item, str) for item in result)