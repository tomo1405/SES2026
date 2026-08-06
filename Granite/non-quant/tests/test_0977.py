import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src_0977 import task_func
import pytest

def test_task_func_input_type():
    with pytest.raises(ValueError) as excinfo:
        task_func("not an array")
    assert "Input must be a 2D numpy array." in str(excinfo.value)

def test_task_func_input_ndim():
    with pytest.raises(ValueError) as excinfo:
        task_func(np.array([1, 2, 3]))
    assert "Input must be a 2D numpy array." in str(excinfo.value)

def test_task_func_output_type():
    records = np.array([[1, 2, 3], [4, 5, 6]])
    result = task_func(records)
    assert isinstance(result, pd.DataFrame)

def test_task_func_output_columns():
    records = np.array([[1, 2, 3], [4, 5, 6]])
    result = task_func(records)
    expected_columns = [f"f{i+1}" for i in range(records[0].shape[0])]
    assert result.columns.tolist() == expected_columns

def test_task_func_output_values():
    records = np.array([[1, 2, 3], [4, 5, 6]])
    result = task_func(records)
    scaler = StandardScaler()
    expected_values = scaler.fit_transform(records.copy()).T
    assert np.array_equal(result.values, expected_values)