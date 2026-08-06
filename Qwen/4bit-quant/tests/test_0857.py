import pytest
from src_0857 import task_func
import numpy as np

def test_task_func_default_values():
    result, matrix = task_func()
    assert matrix.shape == (3, 3)
    assert np.all(matrix >= 1)
    assert np.all(matrix < 10)

def test_task_func_custom_shape():
    result, matrix = task_func(shape=(2, 4))
    assert matrix.shape == (2, 4)
    assert np.all(matrix >= 1)
    assert np.all(matrix < 10)

def test_task_func_custom_range():
    result, matrix = task_func(low=5, high=15)
    assert np.all(matrix >= 5)
    assert np.all(matrix < 15)

def test_task_func_seed():
    result1, matrix1 = task_func(seed=42)
    result2, matrix2 = task_func(seed=42)
    assert np.array_equal(matrix1, matrix2)
    assert result1 == result2

def test_task_func_invalid_range():
    with pytest.raises(ValueError):
        task_func(low=10, high=10)

def test_task_func_invalid_high():
    with pytest.raises(ValueError):
        task_func(low=10, high=9)