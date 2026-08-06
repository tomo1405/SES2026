import pytest
from src_0822 import task_func

def test_task_func():
    results = task_func()
    assert len(results) == 5
    assert all(isinstance(result, str) for result in results)