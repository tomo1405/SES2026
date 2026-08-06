import pytest
from src_0949 import task_func
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def test_task_func_default_parameters():
    expected_rows = 3
    expected_columns = 2
    expected_seed = 42
    
    result = task_func()
    
    assert result.shape == (expected_rows, expected_columns), "Resulting matrix does not have the expected shape."
    
    np.random.seed(expected_seed)
    original_matrix = np.random.rand(expected_rows, expected_columns)
    scaler = MinMaxScaler()
    expected_result = scaler.fit_transform(original_matrix)
    
    assert np.allclose(result, expected_result), "The scaled matrix does not match the expected output."

def test_task_func_custom_parameters():
    custom_rows = 5
    custom_columns = 4
    custom_seed = 100
    
    result = task_func(custom_rows, custom_columns, custom_seed)
    
    assert result.shape == (custom_rows, custom_columns), "Resulting matrix does not have the expected shape."
    
    np.random.seed(custom_seed)
    original_matrix = np.random.rand(custom_rows, custom_columns)
    scaler = MinMaxScaler()
    expected_result = scaler.fit_transform(original_matrix)
    
    assert np.allclose(result, expected_result), "The scaled matrix does not match the expected output."

def test_task_func_reproducibility():
    seed = 42
    first_result = task_func(seed=seed)
    second_result = task_func(seed=seed)
    
    assert np.array_equal(first_result, second_result), "Results are not reproducible with the same seed."