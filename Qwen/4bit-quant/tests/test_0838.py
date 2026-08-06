import pytest
from src_0838 import task_func
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func_output_type():
    result = task_func(5, [0, 1], random_seed=42)
    assert isinstance(result, pd.DataFrame), "The output should be a pandas DataFrame."

def test_task_func_columns():
    result = task_func(5, [0, 1], random_seed=42)
    expected_columns = ['A', 'B', 'C', 'D', 'E']
    assert list(result.columns) == expected_columns, "The DataFrame should have the correct columns."

def test_task_func_scaled_columns():
    result = task_func(5, [0, 1], random_seed=42)
    scaler = StandardScaler()
    scaled_A = scaler.fit_transform(result[['A']])
    scaled_B = scaler.fit_transform(result[['B']])
    np.testing.assert_array_almost_equal(scaled_A, result['A'].values.reshape(-1, 1), decimal=6, err_msg="Column 'A' is not correctly scaled.")
    np.testing.assert_array_almost_equal(scaled_B, result['B'].values.reshape(-1, 1), decimal=6, err_msg="Column 'B' is not correctly scaled.")

def test_task_func_unscaled_columns():
    result = task_func(5, [0, 1], random_seed=42)
    assert result['C'].min() >= 0 and result['C'].max() <= 99, "Column 'C' should not be scaled."
    assert result['D'].min() >= 0 and result['D'].max() <= 99, "Column 'D' should not be scaled."
    assert result['E'].min() >= 0 and result['E'].max() <= 99, "Column 'E' should not be scaled."

def test_task_func_random_seed():
    result1 = task_func(5, [0, 1], random_seed=42)
    result2 = task_func(5, [0, 1], random_seed=42)
    pd.testing.assert_frame_equal(result1, result2, check_dtype=False, check_exact=False, err_msg="Results with the same random seed should be identical.")

def test_task_func_no_scale():
    result = task_func(5, [], random_seed=42)
    assert result.equals(pd.DataFrame(np.random.randint(0, 100, size=(5, 5)), columns=['A', 'B', 'C', 'D', 'E'])), "No columns should be scaled if scale_cols is empty."

def test_task_func_invalid_scale_cols():
    with pytest.raises(IndexError):
        task_func(5, [5], random_seed=42)

def test_task_func_invalid_columns_length():
    with pytest.raises(IndexError):
        task_func(5, [0], columns=['A'], random_seed=42)