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

def test_task_func_with_zero_total_numbers():
    T1 = [['0', '0'], ['0', '0']]
    p25, p50, p75 = task_func(T1)
    assert p25 == 0.0
    assert p50 == 0.0
    assert p75 == 0.0

def test_task_func_with_max_value_zero():
    T1 = [['1', '2'], ['3', '4']]
    with pytest.raises(ValueError):
        task_func(T1, max_value=0)

def test_task_func_with_large_max_value():
    T1 = [['1', '2'], ['3', '4']]
    p25, p50, p75 = task_func(T1, max_value=1000)
    assert isinstance(p25, float)
    assert isinstance(p50, float)
    assert isinstance(p75, float)

def test_task_func_with_negative_max_value():
    T1 = [['1', '2'], ['3', '4']]
    with pytest.raises(ValueError):
        task_func(T1, max_value=-1)