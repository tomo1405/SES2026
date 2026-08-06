import pytest
from src_0857 import task_func
import numpy as np

def test_task_func_default_parameters():
    result, matrix = task_func()
    assert matrix.shape == (3, 3)
    assert 1 <= np.min(matrix) <= 9
    assert 10 > np.max(matrix) >= 1

def test_task_func_custom_shape():
    result, matrix = task_func((2, 2))
    assert matrix.shape == (2, 2)

def test_task_func_custom_range():
    result, matrix = task_func(low=5, high=15)
    assert 5 <= np.min(matrix) <= 14
    assert 15 > np.max(matrix) >= 5

def test_task_func_seed():
    result1, matrix1 = task_func(seed=42)
    result2, matrix2 = task_func(seed=42)
    assert np.array_equal(matrix1, matrix2)
    assert result1 == result2

def test_task_func_invalid_high_low():
    with pytest.raises(ValueError):
        task_func(high=5, low=5)

def test_task_func_invalid_high_less_than_low():
    with pytest.raises(ValueError):
        task_func(high=3, low=5)