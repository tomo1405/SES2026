import pytest
from src_0914 import task_func

def test_task_func():
    data = [1, 2, 3, 2, 2, 1, 4, 5, 4, 3, 2, 1]
    repetitions = 3
    expected_result = {'mode': np.array([2, 1]), 'count': np.array([6, 6]), 'fft': ...}  # Replace ... with the expected FFT result
    result = task_func(data, repetitions)
    assert result == expected_result

def test_task_func_empty_data():
    data = []
    repetitions = 1
    expected_result = {'mode': np.array([], dtype='object'), 'count': np.array([], dtype=int), 'fft': np.array([])}
    result = task_func(data, repetitions)
    assert result == expected_result

def test_task_func_no_repetitions():
    data = [1, 2, 3, 2, 2, 1, 4, 5, 4, 3, 2, 1]
    repetitions = 0
    expected_result = {'mode': np.array([], dtype='object'), 'count': np.array([], dtype=int), 'fft': np.array([])}
    result = task_func(data, repetitions)
    assert result == expected_result