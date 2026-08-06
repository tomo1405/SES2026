import pytest
from src_0441 import task_func
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Test cases for the function

def test_task_func_basic():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[5, 6], [7, 8]])
    result = task_func(P, T)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (2, 2)

def test_task_func_empty_input():
    P = np.array([])
    T = np.array([])
    with pytest.raises(ValueError):
        task_func(P, T)

def test_task_func_incompatible_shapes():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([5, 6])
    with pytest.raises(ValueError):
        task_func(P, T)

def test_task_func_scaler():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[5, 6], [7, 8]])
    result = task_func(P, T)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (2, 2)
    assert np.allclose(result.iloc[:, 0], (1, 3))