import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from src_0979 import task_func
import pytest

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func("invalid input")

def test_task_func_empty_array():
    array = np.array([])
    expected_output = pd.DataFrame(columns=["PC1", "PC2"])
    actual_output = task_func(array)
    assert actual_output.equals(expected_output)

def test_task_func_1d_array():
    array = np.array([1, 2, 3])
    with pytest.raises(ValueError):
        task_func(array)

def test_task_func_2d_array():
    array = np.array([[1, 2, 3], [4, 5, 6]])
    expected_output = pd.DataFrame(data=[[3.5, 6.5], [3.5, 6.5]], columns=["PC1", "PC2"])
    actual_output = task_func(array)
    assert actual_output.equals(expected_output)

def test_task_func_2d_array_with_seed():
    array = np.array([[1, 2, 3], [4, 5, 6]])
    seed = 42
    expected_output = pd.DataFrame(data=[[3.5, 6.5], [3.5, 6.5]], columns=["PC1", "PC2"])
    actual_output = task_func(array, seed=seed)
    assert actual_output.equals(expected_output)