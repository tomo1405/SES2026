import pytest
from src_0822 import task_func

def test_task_func_default():
    expected_results = [
        'Delay in thread 0 completed',
        'Delay in thread 1 completed',
        'Delay in thread 2 completed',
        'Delay in thread 3 completed',
        'Delay in thread 4 completed'
    ]
    assert task_func() == expected_results

def test_task_func_custom_delay():
    expected_results = [
        'Delay in thread 0 completed',
        'Delay in thread 1 completed',
        'Delay in thread 2 completed',
        'Delay in thread 3 completed',
        'Delay in thread 4 completed'
    ]
    assert task_func(delay_time=2.0) == expected_results

def test_task_func_custom_threads():
    expected_results = [
        'Delay in thread 0 completed',
        'Delay in thread 1 completed'
    ]
    assert task_func(num_threads=2) == expected_results

def test_task_func_zero_threads():
    expected_results = []
    assert task_func(num_threads=0) == expected_results

def test_task_func_negative_threads():
    with pytest.raises(ValueError):
        task_func(num_threads=-1)

def test_task_func_non_positive_delay():
    with pytest.raises(ValueError):
        task_func(delay_time=0.0)
    with pytest.raises(ValueError):
        task_func(delay_time=-1.0)