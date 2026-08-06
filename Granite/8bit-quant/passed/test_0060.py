import pytest
from src_0060 import task_func

def test_task_func():
    # Test case 1: Valid input
    page_title = "Python"
    ax = task_func(page_title)
    assert ax is not None

    # Test case 2: Invalid input
    page_title = "Invalid Page"
    ax = task_func(page_title)
    assert ax is None