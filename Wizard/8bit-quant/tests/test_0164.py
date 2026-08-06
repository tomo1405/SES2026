python
import pytest
from src_0164 import task_func

def test_task_func():
    ax = task_func(rows=5, cols=5)
    assert ax is not None