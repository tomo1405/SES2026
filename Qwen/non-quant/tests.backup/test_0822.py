import pytest
from src_0822 import task_func

def test_task_func_default_parameters():
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
        'Delay in thread 2 completed'
    ]
    assert task_func(delay_time=0.5, num_threads=3) == expected_results

def test_task_func_single_thread():
    expected_results = ['Delay in thread 0 completed']
    assert task_func(num_threads=1) == expected_results

def test_task_func_no_threads():
    expected_results = []
    assert task_func(num_threads=0) == expected_results

def test_task_func_large_number_of_threads():
    num_threads = 10
    expected_results = [f'Delay in thread {i} completed' for i in range(num_threads)]
    assert task_func(num_threads=num_threads) == expected_results