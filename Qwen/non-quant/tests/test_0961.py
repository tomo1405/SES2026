import random

import pytest
from src_0961 import task_func


def test_task_func_with_empty_text():
    with pytest.raises(ValueError):
        task_func("")

def test_task_func_with_alpha_text():
    random.seed(0)
    result = task_func("abc")
    assert result == "rpl"

def test_task_func_with_digit_text():
    random.seed(0)
    result = task_func("123")
    assert result == "789"

def test_task_func_with_mixed_text():
    random.seed(0)
    result = task_func("a1 b")
    assert result == "r7l"

def test_task_func_with_special_chars():
    random.seed(0)
    result = task_func("!@#")
    assert result == "!@#"

def test_task_func_with_seed():
    random.seed(0)
    result1 = task_func("abc", seed=0)
    random.seed(0)
    result2 = task_func("abc", seed=0)
    assert result1 == result2

def test_task_func_without_seed():
    result1 = task_func("abc")
    result2 = task_func("abc")
    assert result1 != result2