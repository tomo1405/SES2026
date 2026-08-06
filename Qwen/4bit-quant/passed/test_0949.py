import pytest
from src_0949 import task_func
import numpy as np

def test_task_func_default_values():
    expected_shape = (3, 2)
    result = task_func()
    assert result.shape == expected_shape, "The shape of the result does not match the expected shape."

def test_task_func_custom_dimensions():
    expected_shape = (5, 3)
    result = task_func(rows=5, columns=3)
    assert result.shape == expected_shape, "The shape of the result does not match the expected shape."

def test_task_func_reproducibility():
    first_run = task_func()
    second_run = task_func()
    assert np.array_equal(first_run, second_run), "The results are not reproducible with the same seed."

def test_task_func_min_max_values():
    result = task_func()
    assert np.all(result >= 0) and np.all(result <= 1), "The scaled values are not within the range [0, 1]."

def test_task_func_randomness():
    result = task_func(seed=42)
    assert not np.allclose(result, np.zeros_like(result)), "The result is not random."