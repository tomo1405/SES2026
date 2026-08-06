import pytest
from src_1033 import task_func

def test_task_func():
    ax = task_func()
    assert ax is not None

def test_task_func_with_data():
    ax = task_func(rows=100, string_length=5)
    assert ax is not None

def test_task_func_with_empty_data():
    ax = task_func(rows=0, string_length=5)
    assert ax is None