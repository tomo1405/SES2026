import pytest
from src_0979 import task_func
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

def test_task_func_basic():
    # Test with a valid 2D numpy array
    array = np.array([[1, 2, 3], [4, 5, 6]])
    result = task_func(array)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (2, 2)

def test_task_func_empty():
    # Test with an empty 2D numpy array
    array = np.array([[]])
    result = task_func(array)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (0, 2)

def test_task_func_seed():
    # Test with seed
    array = np.array([[1, 2, 3], [4, 5, 6]])
    result1 = task_func(array, seed=42)
    result2 = task_func(array, seed=42)
    assert np.array_equal(result1, result2)

def test_task_func_invalid_input():
    # Test with an invalid input
    with pytest.raises(ValueError):
        task_func(np.array([1, 2, 3]))