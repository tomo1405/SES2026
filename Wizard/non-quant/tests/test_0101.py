python
import pytest
from src_0101 import task_func

def test_task_func():
    try:
        ax = task_func()
        assert ax is not None
    except ValueError as e:
        assert False, f"Error generating the plot: {e}"