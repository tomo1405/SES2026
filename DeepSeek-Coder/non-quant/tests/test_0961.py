import pytest
from src_0961 import task_func

def test_task_func_basic():
    assert task_func("hello", seed=42) == "kqz"

def test_task_func_empty_text():
    with pytest.raises(ValueError):
        task_func("")

def test_task_func_with_seed():
    assert task_func("hello", seed=42) == task_func("hello", seed=42)

def test_task_func_with_spaces():
    assert task_func("hello world", seed=42) == "kqzvix"

def test_task_func_with_digits():
    assert task_func("123", seed=42) == "3"

def test_task_func_with_special_chars():
    assert task_func("!@#", seed=42) == "v"