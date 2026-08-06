python
import time
import threading
import pytest

from src_0822 import task_func

def test_task_func():
    results = task_func()
    assert len(results) == 5
    assert all(isinstance(result, str) for result in results)
    assert all(result.startswith('Delay in thread ') for result in results)
    assert all(result.endswith(' completed') for result in results)