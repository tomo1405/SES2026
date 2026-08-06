import string

import pytest
from src_0961 import task_func


def test_task_func_with_empty_text():
    with pytest.raises(ValueError):
        task_func("")

def test_task_func_with_seed():
    seed = 42
    result1 = task_func("abc123", seed)
    result2 = task_func("abc123", seed)
    assert result1 == result2

def test_task_func_with_alpha_text():
    result = task_func("abc")
    assert all(c in string.ascii_lowercase for c in result)

def test_task_func_with_digit_text():
    result = task_func("123")
    assert all(c in string.digits for c in result)

def test_task_func_with_mixed_text():
    result = task_func("a1 ")
    assert len(result) == 3
    assert result[0] in string.ascii_lowercase
    assert result[1] in string.digits
    assert result[2] in string.ascii_lowercase or string.digits

def test_task_func_with_special_characters():
    result = task_func("!@#")
    assert result == "!@#"

def test_task_func_with_space_handling():
    result = task_func("a 1")
    assert len(result) == 3
    assert result[0] in string.ascii_lowercase
    assert result[1] in string.ascii_lowercase or string.digits
    assert result[2] in string.digits