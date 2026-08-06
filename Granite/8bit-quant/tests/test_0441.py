import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src_0441 import task_func
import pytest

def test_task_func_with_empty_inputs():
    P = np.array([])
    T = np.array([])
    with pytest.raises(ValueError) as excinfo:
        task_func(P, T)
    assert "Inputs cannot be empty." in str(excinfo.value)

def test_task_func_with_incompatible_shapes():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[5, 6]])
    with pytest.raises(ValueError) as excinfo:
        task_func(P, T)
    assert "Matrix P shape 2 and Tensor T shape 1 are incompatible for tensor multiplication." in str(excinfo.value)

def test_task_func_with_valid_inputs():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[5, 6], [7, 8]])
    result = task_func(P, T)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (2, 4)
    assert result.columns.tolist() == ["feature_0", "feature_1", "feature_2", "feature_3"]