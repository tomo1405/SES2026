import pytest
from src_0441 import task_func
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[5, 6], [7, 8]])
    result = task_func(P, T)
    assert result.shape == (2, 2)
    assert result.columns.tolist() == ["feature_0", "feature_1"]

def test_task_func_empty_input():
    P = np.array([])
    T = np.array([])
    with pytest.raises(ValueError):
        task_func(P, T)

def test_task_func_incompatible_shapes():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[5, 6], [7, 8], [9, 10]])
    with pytest.raises(ValueError):
        task_func(P, T)

def test_task_func_scaling():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[5, 6], [7, 8]])
    result = task_func(P, T)
    scaler = StandardScaler()
    expected_result = scaler.fit_transform(result)
    assert np.allclose(result, expected_result)

def test_task_func_adjusted_feature_names():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[5, 6], [7, 8]])
    result = task_func(P, T)
    expected_feature_names = [f"feature_{i}" for i in range(result.shape[1])]
    assert result.columns.tolist() == expected_feature_names