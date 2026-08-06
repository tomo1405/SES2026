import pytest
from src_0060 import task_func

def test_task_func():
    # Test case 1: page_title is a valid string
    ax = task_func("Python_(programming_language)")
    assert ax is not None

    # Test case 2: page_title is an invalid string
    ax = task_func("Invalid_page_title")
    assert ax is None

    # Test case 3: page_title is a string with special characters
    ax = task_func("Pyth҆!@#$%^&*()")
    assert ax is None