python
import time
import threading
import pytest

from src_0822 import task_func

def test_task_func():
    results = task_func()
    assert len(results) == 5
    for result in results:
        assert 'Delay in thread' in result