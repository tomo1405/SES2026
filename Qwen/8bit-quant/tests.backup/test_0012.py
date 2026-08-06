import pytest
from src_0012 import task_func
import numpy as np

def test_task_func_with_single_element():
    T1 = [['1']]
    p25, p50, p75 = task_func(T1)
    assert isinstance(p25, float)
    assert isinstance(p50, float)
    assert isinstance(p75, float)

def test_task_func_with_multiple_elements():
    T1 = [['1', '2'], ['3', '4']]
    p25, p50, p75 = task_func(T1)
    assert isinstance(p25, float)
    assert isinstance(p50, float)
    assert isinstance(p75, float)

def test_task_func_with_zero_elements():
    T1 = [[]]
    p25, p50, p75 = task_func(T1)
    assert np.isnan(p25)
    assert np.isnan(p50)
    assert np.isnan(p75)

def test_task_func_with_max_value():
    T1 = [['1', '2'], ['3', '4']]
    max_value = 50
    p25, p50, p75 = task_func(T1, max_value=max_value)
    assert isinstance(p25, float)
    assert isinstance(p50, float)
    assert isinstance(p75, float)
    assert all(0 <= num <= max_value for num in [p25, p50, p75])

def test_task_func_with_negative_numbers():
    T1 = [['-1', '-2'], ['-3', '-4']]
    with pytest.raises(ValueError):
        task_func(T1)

def test_task_func_with_non_numeric_strings():
    T1 = [['a', 'b'], ['c', 'd']]
    with pytest.raises(ValueError):
        task_func(T1)