import numpy as np
import pytest
from src_0653 import task_func


def test_task_func():
    target_value = '332'
    array = np.array([['0', '1', '2'], ['a', 'bb', 'ccc'], ['332', '33', '2'], ['33', '22', '332']])
    mean, variance, skewness, kurtosis = task_func(target_value, array)
    assert isinstance(mean, float)
    assert isinstance(variance, float)
    assert isinstance(skewness, float)
    assert isinstance(kurtosis, float)

def test_task_func_not_enough_data():
    target_value = '332'
    array = np.array([['0', '1', '2'], ['a', 'bb', 'ccc'], ['332', '33', '2']])
    mean, variance, skewness, kurtosis = task_func(target_value, array)
    assert mean == 'N/A'
    assert variance == 'N/A'
    assert skewness == 'N/A'
    assert kurtosis == 'N/A'

def test_task_func_plot():
    target_value = '332'
    array = np.array([['0', '1', '2'], ['a', 'bb', 'ccc'], ['332', '33', '2'], ['33', '22', '332']])
    with pytest.warns(UserWarning):
        mean, variance, skewness, kurtosis = task_func(target_value, array)
    assert mean == 2.0
    assert variance == 0.0
    assert skewness == 0.0
    assert kurtosis == -2.0