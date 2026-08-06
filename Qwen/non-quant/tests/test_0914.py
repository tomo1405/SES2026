import numpy as np
from src_0914 import task_func


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
    result = task_func([1, 2, 2, 3])
    assert np.array_equal(result['mode'], np.array([2]))
    assert np.array_equal(result['count'], np.array([2]))
    assert np.allclose(result['fft'], np.fft.fft([1, 2, 2, 3]))

def test_task_func_multiple_modes():
    result = task_func([1, 1, 2, 2, 3, 3])
    assert np.array_equal(result['mode'], np.array([1, 2, 3]))
    assert np.array_equal(result['count'], np.array([2, 2, 2]))
    assert np.allclose(result['fft'], np.fft.fft([1, 1, 2, 2, 3, 3]))

def test_task_func_with_repetitions():
    result = task_func([1, 2, 3], repetitions=2)
    assert np.array_equal(result['mode'], np.array([1, 2, 3]))
    assert np.array_equal(result['count'], np.array([2, 2, 2]))
    assert np.allclose(result['fft'], np.fft.fft([1, 2, 3]))

def test_task_func_with_strings():
    result = task_func(['a', 'b', 'b', 'c'])
    assert np.array_equal(result['mode'], np.array(['b']))
    assert np.array_equal(result['count'], np.array([2]))
    assert np.allclose(result['fft'], np.fft.fft(['a', 'b', 'b', 'c']))

def test_task_func_mixed_types():
    result = task_func([1, '1', 2, '2', 2, '2'])
    assert np.array_equal(result['mode'], np.array([2, '2']))
    assert np.array_equal(result['count'], np.array([2, 2]))
    assert np.allclose(result['fft'], np.fft.fft([1, '1', 2, '2', 2, '2']))