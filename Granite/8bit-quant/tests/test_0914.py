import numpy as np
from src_0914 import task_func


def test_task_func():
    data = [1, 2, 3, 4, 5]
    repetitions = 3
    expected_result = {'mode': np.array([1, 2, 3, 4, 5], dtype='object'),
                       'count': np.array([3, 3, 3, 3, 3], dtype=int),
                       'fft': ...}  # Replace with the expected FFT result
    result = task_func(data, repetitions)
    assert result == expected_result

def test_task_func_empty_data():
    data = []
    repetitions = 1
    expected_result = {'mode': np.array([], dtype='object'),
                       'count': np.array([], dtype=int),
                       'fft': np.array([])}
    result = task_func(data, repetitions)
    assert result == expected_result

def test_task_func_no_repetitions():
    data = [1, 2, 3, 4, 5]
    repetitions = 0
    expected_result = {'mode': np.array([], dtype='object'),
                       'count': np.array([], dtype=int),
                       'fft': np.array([])}
    result = task_func(data, repetitions)
    assert result == expected_result