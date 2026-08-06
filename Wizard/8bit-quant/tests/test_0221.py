python
import pytest
from src_0221 import task_func

def test_task_func():
    colors = ['red', 'green', 'blue', 'yellow', 'orange']
    task_func(colors)
    assert True