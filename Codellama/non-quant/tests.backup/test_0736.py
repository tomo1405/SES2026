import pytest
from src_0736 import task_func
import numpy as np

def test_task_func():
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = task_func(L)
    assert result['mean'] == 5.0
    assert result['variance'] == 2.0

def test_task_func_empty_list():
    L = []
    result = task_func(L)
    assert result['mean'] == 0.0
    assert result['variance'] == 0.0

def test_task_func_single_element_list():
    L = [[1]]
    result = task_func(L)
    assert result['mean'] == 1.0
    assert result['variance'] == 0.0

def test_task_func_negative_values():
    L = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
    result = task_func(L)
    assert result['mean'] == -5.0
    assert result['variance'] == 2.0

def test_task_func_mixed_values():
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, -2, -3]]
    result = task_func(L)
    assert result['mean'] == 2.0
    assert result['variance'] == 2.0