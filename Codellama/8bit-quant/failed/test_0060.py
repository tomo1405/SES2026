import pytest
from src_0060 import task_func

def test_task_func_valid_input():
    page_title = "Python (programming language)"
    ax = task_func(page_title)
    assert ax is not None

def test_task_func_invalid_input():
    page_title = "Invalid page title"
    ax = task_func(page_title)
    assert ax is None