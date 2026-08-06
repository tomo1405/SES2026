import pytest
from src_1089 import task_func
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func_default_data():
    result = task_func()
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (100, 5)
    assert all(result.columns == [0, 1, 2, 3, 4])

def test_task_func_custom_data():
    custom_data = np.array([[0.6, 0.7, 0.8, 0.9, 1.0], [0.1, 0.2, 0.3, 0.4, 0.5]])
    result = task_func(custom_data)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (2, 5)
    assert all(result.columns == [0, 1, 2, 3, 4])

def test_task_func_data_below_threshold():
    custom_data = np.array([[0.4, 0.5, 0.6, 0.7, 0.8], [0.1, 0.2, 0.3, 0.4, 0.5]])
    result = task_func(custom_data)
    assert result.iloc[0].sum() == 0  # All values below 0.5 should be set to 0
    assert result.iloc[1].sum() > 0  # Values above 0.5 should remain unchanged

def test_task_func_scaling():
    custom_data = np.array([[0.6, 0.7, 0.8, 0.9, 1.0], [0.1, 0.2, 0.3, 0.4, 0.5]])
    result = task_func(custom_data)
    scaler = StandardScaler()
    expected_scaled_data = scaler.fit_transform(pd.DataFrame(custom_data))
    expected_df = pd.DataFrame(expected_scaled_data, columns=[0, 1, 2, 3, 4])
    assert result.equals(expected_df)

def test_task_func_column_names():
    custom_data = np.array([[0.6, 0.7, 0.8, 0.9, 1.0], [0.1, 0.2, 0.3, 0.4, 0.5]])
    result = task_func(custom_data)
    assert all(result.columns == [0, 1, 2, 3, 4])

def test_task_func_data_types():
    custom_data = np.array([[0.6, 0.7, 0.8, 0.9, 1.0], [0.1, 0.2, 0.3, 0.4, 0.5]])
    result = task_func(custom_data)
    assert all(isinstance(value, np.float64) for value in result.values.flatten())