import pytest
from src_0144 import task_func

def test_task_func():
    # Assuming the function returns a matplotlib Axes object
    ax = task_func()
    assert ax is not None, "The function did not return a valid Axes object"