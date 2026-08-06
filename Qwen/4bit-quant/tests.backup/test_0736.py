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
    result = task_func([[1, 2, 3], [4, 5]])
    assert result == {'mean': 3.0, 'variance': 2.5}

def test_task_func_with_nested_lists():
    result = task_func([[1, [2, 3]], [4, 5]])
    assert result == {'mean': 3.0, 'variance': 2.5}

def test_task_func_with_negative_numbers():
    result = task_func([[-1, -2, -3], [-4, -5]])
    assert result == {'mean': -3.0, 'variance': 2.5}

def test_task_func_with_mixed_types():
    with pytest.raises(TypeError):
        task_func([[1, 'a'], [2, 3]])

def test_task_func_with_non_numeric_values():
    with pytest.raises(TypeError):
        task_func([['a', 'b'], ['c', 'd']])