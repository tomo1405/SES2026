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

def test_task_func_single_mode():
    result = task_func([1, 1, 2, 2, 3])
    assert np.array_equal(result['mode'], np.array([1]))
    assert np.array_equal(result['count'], np.array([2]))
    np.testing.assert_array_almost_equal(result['fft'], scipy.fft.fft([1, 1, 2, 2, 3]))

def test_task_func_multiple_modes():
    result = task_func([1, 1, 2, 2, 3, 3])
    assert np.array_equal(result['mode'], np.array([1, 2, 3]))
    assert np.array_equal(result['count'], np.array([2, 2, 2]))
    np.testing.assert_array_almost_equal(result['fft'], scipy.fft.fft([1, 1, 2, 2, 3, 3]))

def test_task_func_with_repetitions():
    result = task_func([1, 2, 3], repetitions=3)
    assert np.array_equal(result['mode'], np.array([1, 2, 3]))
    assert np.array_equal(result['count'], np.array([3, 3, 3]))
    np.testing.assert_array_almost_equal(result['fft'], scipy.fft.fft([1, 2, 3]))

def test_task_func_with_strings():
    result = task_func(['a', 'a', 'b', 'b', 'c'])
    assert np.array_equal(result['mode'], np.array(['a', 'b']))
    assert np.array_equal(result['count'], np.array([2, 2]))
    np.testing.assert_array_almost_equal(result['fft'], scipy.fft.fft(['a', 'a', 'b', 'b', 'c']))

def test_task_func_with_mixed_types():
    result = task_func([1, '1', 2, '2', 3])
    assert np.array_equal(result['mode'], np.array([1, '1', 2, '2', 3]))
    assert np.array_equal(result['count'], np.array([1, 1, 1, 1, 1]))
    np.testing.assert_array_almost_equal(result['fft'], scipy.fft.fft([1, '1', 2, '2', 3]))

def test_task_func_with_large_repetitions():
    result = task_func([1, 2, 3], repetitions=100)
    assert np.array_equal(result['mode'], np.array([1, 2, 3]))
    assert np.array_equal(result['count'], np.array([100, 100, 100]))
    np.testing.assert_array_almost_equal(result['fft'], scipy.fft.fft([1, 2, 3]))