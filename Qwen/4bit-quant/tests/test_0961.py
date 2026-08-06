import string

import pytest
from src_0961 import task_func


def test_task_func_with_empty_text():
    with pytest.raises(ValueError):
        task_func("")

def test_task_func_with_seed():
    seed = 42
    result1 = task_func("Hello World!", seed=seed)
    result2 = task_func("Hello World!", seed=seed)
    assert result1 == result2

def test_task_func_with_alpha_characters():
    result = task_func("Hello")
    assert all(c.islower() for c in result)

def test_task_func_with_digit_characters():
    result = task_func("12345")
    assert all(c.isdigit() for c in result)

def test_task_func_with_space_characters():
    result = task_func("Hello World!")
    spaces = [i for i, c in enumerate(result) if c in string.ascii_lowercase + string.digits]
    assert len(spaces) == 1

def test_task_func_with_special_characters():
    result = task_func("Hello!@#")
    special_chars = "!@#"
    assert all(c in special_chars for c in result if c not in string.ascii_lowercase and c not in string.digits)

def test_task_func_with_mixed_characters():
    result = task_func("H3llo W0rld!")
    assert all(c.islower() for c in result if c in string.ascii_lowercase)
    assert all(c.isdigit() for c in result if c in string.digits)
    assert len([c for c in result if c in string.ascii_lowercase + string.digits]) == 1