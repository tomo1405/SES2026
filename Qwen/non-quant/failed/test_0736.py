import pytest
from src_0736 import task_func
import numpy as np

def test_task_func_with_empty_list():
    result = task_func([])
    assert result == {'mean': np.nan, 'variance': np.nan}

def test_task_func_with_single_element():
    result = task_func([[5]])
    assert result == {'mean': 5.0, 'variance': 0.0}

def test_task_func_with_multiple_elements():
    result = task_func([[1, 2], [3, 4]])
    assert result == {'mean': 2.5, 'variance': 1.25}

def test_task_func_with_nested_lists():
    result = task_func([[[1, 2], [3]], [4, 5]])
    assert result == {'mean': 3.0, 'variance': 2.0}

def test_task_func_with_negative_numbers():
    result = task_func([[-1, -2], [-3, -4]])
    assert result == {'mean': -2.5, 'variance': 1.25}

def test_task_func_with_mixed_positive_and_negative_numbers():
    result = task_func([[1, -2], [3, -4]])
    assert result == {'mean': -0.5, 'variance': 6.25}

def test_task_func_with_floats():
    result = task_func([[1.5, 2.5], [3.5, 4.5]])
    assert np.isclose(result['mean'], 3.0) and np.isclose(result['variance'], 1.25)

def test_task_func_with_large_numbers():
    result = task_func([[1000000, 2000000], [3000000, 4000000]])
    assert result == {'mean': 2500000.0, 'variance': 500000000000.0}