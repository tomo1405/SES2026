import pytest
from src_0441 import task_func
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func_empty_input():
    P = np.array([])
    T = np.array([])
    with pytest.raises(ValueError, match="Inputs cannot be empty."):
        task_func(P, T)

def test_task_func_incompatible_shapes():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[5, 6], [7, 8], [9, 10]])
    with pytest.raises(ValueError, match="Matrix P shape 2 and Tensor T shape 3 are incompatible for tensor multiplication."):
        task_func(P, T)

def test_task_func_valid_input():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[5, 6], [7, 8]])
    expected_result = np.array([[19, 22], [43, 50]])
    expected_df = pd.DataFrame(StandardScaler().fit_transform(expected_result), columns=["feature_0", "feature_1"])
    
    result_df = task_func(P, T)
    
    assert result_df.equals(expected_df)

def test_task_func_single_element():
    P = np.array([[1]])
    T = np.array([[2]])
    expected_result = np.array([[2]])
    expected_df = pd.DataFrame(StandardScaler().fit_transform(expected_result), columns=["feature_0"])
    
    result_df = task_func(P, T)
    
    assert result_df.equals(expected_df)

def test_task_func_multiple_features():
    P = np.array([[1, 2, 3], [4, 5, 6]])
    T = np.array([[7, 8], [9, 10], [11, 12]])
    expected_result = np.array([[58, 64], [139, 154]])
    expected_df = pd.DataFrame(StandardScaler().fit_transform(expected_result), columns=["feature_0", "feature_1"])
    
    result_df = task_func(P, T)
    
    assert result_df.equals(expected_df)