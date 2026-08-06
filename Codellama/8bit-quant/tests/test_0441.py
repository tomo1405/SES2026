import pytest
from src_0441 import task_func
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func_empty_inputs():
    with pytest.raises(ValueError):
        task_func(np.array([]), np.array([]))

def test_task_func_incompatible_shapes():
    with pytest.raises(ValueError):
        task_func(np.array([[1, 2], [3, 4]]), np.array([[1, 2], [3, 4]]))

def test_task_func_valid_inputs():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[1, 2], [3, 4]])
    result = task_func(P, T)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (2, 2)
    assert result.columns.tolist() == ["feature_0", "feature_1"]

def test_task_func_scaling():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[1, 2], [3, 4]])
    result = task_func(P, T)
    scaler = StandardScaler()
    expected_result = scaler.fit_transform(result)
    assert np.allclose(result, expected_result)