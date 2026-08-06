import pytest
from src_0822 import task_func

def test_task_func():
    results = task_func()
    assert isinstance(results, list)
    for result in results:
        assert isinstance(result, str)

def test_task_func_with_delay():
    results = task_func(delay_time=0.5)
    assert len(results) == 5
    for result in results:
        assert 'Delay in thread' in result

def test_task_func_with_num_threads():
    results = task_func(num_threads=10)
    assert len(results) == 10
    for result in results:
        assert 'Delay in thread' in result

def test_task_func_with_delay_and_num_threads():
    results = task_func(delay_time=0.5, num_threads=10)
    assert len(results) == 10
    for result in results:
        assert 'Delay in thread' in result