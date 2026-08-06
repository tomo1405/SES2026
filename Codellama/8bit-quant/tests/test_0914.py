import numpy as np
from src_0914 import task_func


def test_task_func_empty_data():
    data = []
    repetitions = 1
    result = task_func(data, repetitions)
    assert result == {'mode': np.array([], dtype='object'), 'count': np.array([], dtype=int), 'fft': np.array([])}


def test_task_func_no_repetitions():
    data = [1, 2, 3]
    repetitions = 0
    result = task_func(data, repetitions)
    assert result == {'mode': np.array([], dtype='object'), 'count': np.array([], dtype=int), 'fft': np.array([])}


def test_task_func_single_repetition():
    data = [1, 2, 3]
    repetitions = 1
    result = task_func(data, repetitions)
    assert result == {'mode': np.array([1, 2, 3], dtype='object'), 'count': np.array([1, 1, 1], dtype=int), 'fft': np.array([])}


def test_task_func_multiple_repetitions():
    data = [1, 2, 3]
    repetitions = 3
    result = task_func(data, repetitions)
    assert result == {'mode': np.array([1, 2, 3], dtype='object'), 'count': np.array([3, 3, 3], dtype=int), 'fft': np.array([])}


def test_task_func_mixed_data():
    data = [1, 'a', 2, 'b', 3]
    repetitions = 2
    result = task_func(data, repetitions)
    assert result == {'mode': np.array([1, 'a', 2, 'b', 3], dtype='object'), 'count': np.array([2, 2, 2, 2, 2], dtype=int), 'fft': np.array([])}


def test_task_func_fft():
    data = [1, 2, 3]
    repetitions = 1
    result = task_func(data, repetitions)
    assert result == {'mode': np.array([1, 2, 3], dtype='object'), 'count': np.array([1, 1, 1], dtype=int), 'fft': np.array([])}