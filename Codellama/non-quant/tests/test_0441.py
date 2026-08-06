import pytest
from src_0441 import task_func
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func_empty_inputs():
    P = np.array([])
    T = np.array([])
    with pytest.raises(ValueError):
        task_func(P, T)

def test_task_func_incompatible_shapes():
    P = np.array([[1, 2, 3], [4, 5, 6]])
    T = np.array([[1, 2], [3, 4]])
    with pytest.raises(ValueError):
        task_func(P, T)

def test_task_func_valid_inputs():
    P = np.array([[1, 2, 3], [4, 5, 6]])
    T = np.array([[1, 2, 3], [4, 5, 6]])
    result = task_func(P, T)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (2, 3)
    assert result.columns.tolist() == ["feature_0", "feature_1", "feature_2"]
    assert np.allclose(result.values, np.array([[1, 2, 3], [4, 5, 6]]))