import pytest
from src_0914 import task_func
import numpy as np
import scipy.fft

def test_task_func_empty_data():
    result = task_func([])
    assert np.array_equal(result['mode'], np.array([], dtype='object'))
    assert np.array_equal(result['count'], np.array([], dtype=int))
    assert np.array_equal(result['fft'], np.array([]))

def test_task_func_no_repetitions():
    result = task_func([1, 2, 3], repetitions=0)
    assert np.array_equal(result['mode'], np.array([], dtype='object'))
    assert np.array_equal(result['count'], np.array([], dtype=int))
    assert np.array_equal(result['fft'], np.array([]))

def test_task_func_single_element():
    result = task_func([1])
    assert np.array_equal(result['mode'], np.array([1], dtype='object'))
    assert np.array_equal(result['count'], np.array([1]))
    assert np.array_equal(result['fft'], np.array([1+0j]))

def test_task_func_multiple_elements():
    result = task_func([1, 2, 2, 3, 3, 3])
    assert np.array_equal(result['mode'], np.array([3], dtype='object'))
    assert np.array_equal(result['count'], np.array([3]))
    assert np.array_equal(result['fft'], scipy.fft.fft([1, 2, 2, 3, 3, 3]))

def test_task_func_repetitions():
    result = task_func([1, 2, 2, 3, 3, 3], repetitions=2)
    assert np.array_equal(result['mode'], np.array([3], dtype='object'))
    assert np.array_equal(result['count'], np.array([6]))
    assert np.array_equal(result['fft'], scipy.fft.fft([1, 2, 2, 3, 3, 3]))

def test_task_func_mixed_types():
    result = task_func([1, '2', '2', 3, 3, 3])
    assert np.array_equal(result['mode'], np.array([3], dtype='object'))
    assert np.array_equal(result['count'], np.array([3]))
    assert np.array_equal(result['fft'], scipy.fft.fft([1, '2', '2', 3, 3, 3]))

def test_task_func_fft_complex():
    result = task_func([1, 2, 3, 4])
    expected_fft = scipy.fft.fft([1, 2, 3, 4])
    assert np.allclose(result['fft'], expected_fft)

def test_task_func_mode_tie_breaker():
    result = task_func([1, 1, 2, 2, 3, 3])
    assert np.array_equal(result['mode'], np.array([1, 2, 3], dtype='object'))
    assert np.array_equal(result['count'], np.array([2, 2, 2]))