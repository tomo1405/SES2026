import pytest
from src_0822 import task_func

def test_task_func():
    results = task_func()
    assert isinstance(results, list)
    for result in results:
        assert isinstance(result, str)

def test_task_func_with_delay():
    delay_time = 2.0
    num_threads = 3
    results = task_func(delay_time, num_threads)
    assert len(results) == num_threads
    for result in results:
        assert 'Delay in thread' in result
        assert 'completed' in result