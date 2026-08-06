import numpy as np
from src_0653 import task_func


def test_task_func_with_valid_input():
    target_value = '332'
    array = np.array([['0', '1', '2'], ['a', 'bb', 'ccc'], ['332', '33', '2'], ['33', '22', '332']])
    mean, variance, skewness, kurtosis = task_func(target_value, array)
    assert mean == 2
    assert variance == 0
    assert skewness == 0
    assert kurtosis == 0

def test_task_func_with_invalid_input():
    target_value = '332'
    array = np.array([['0', '1', '2'], ['a', 'bb', 'ccc'], ['332', '33', '2'], ['33', '22', '332']])
    mean, variance, skewness, kurtosis = task_func(target_value, array)
    assert mean == 'N/A'
    assert variance == 'N/A'
    assert skewness == 'N/A'
    assert kurtosis == 'N/A'

def test_task_func_with_empty_input():
    target_value = '332'
    array = np.array([])
    mean, variance, skewness, kurtosis = task_func(target_value, array)
    assert mean == 'N/A'
    assert variance == 'N/A'
    assert skewness == 'N/A'
    assert kurtosis == 'N/A'