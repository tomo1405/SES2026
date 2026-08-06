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
    expected_result = np.array([[23, 34], [53, 74]])
    expected_result_scaled = StandardScaler().fit_transform(expected_result)
    expected_columns = ['feature_0', 'feature_1']
    
    result = task_func(P, T)
    
    assert isinstance(result, pd.DataFrame)
    assert np.allclose(result.values, expected_result_scaled)
    assert list(result.columns) == expected_columns

def test_task_func_single_element():
    P = np.array([[1]])
    T = np.array([[2]])
    expected_result = np.array([[2]])
    expected_result_scaled = StandardScaler().fit_transform(expected_result)
    expected_columns = ['feature_0']
    
    result = task_func(P, T)
    
    assert isinstance(result, pd.DataFrame)
    assert np.allclose(result.values, expected_result_scaled)
    assert list(result.columns) == expected_columns

def test_task_func_multiple_features():
    P = np.array([[1, 2, 3], [4, 5, 6]])
    T = np.array([[7, 8], [9, 10], [11, 12]])
    expected_result = np.array([[58, 64], [139, 154]])
    expected_result_scaled = StandardScaler().fit_transform(expected_result)
    expected_columns = ['feature_0', 'feature_1']
    
    result = task_func(P, T)
    
    assert isinstance(result, pd.DataFrame)
    assert np.allclose(result.values, expected_result_scaled)
    assert list(result.columns) == expected_columns