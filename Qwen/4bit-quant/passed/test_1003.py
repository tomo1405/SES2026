import pytest
from src_1003 import task_func
import pandas as pd
import numpy as np

def test_task_func_with_valid_data():
    data = {'target_column': [1, 2, 3, 4, 5]}
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert 'target_column' in df.columns
    assert df['target_column'].dtype == np.int64
    assert ax.get_title() == 'Histogram of target_column'
    assert ax.get_xlabel() == 'target_column'

def test_task_func_with_non_numeric_data():
    data = {'target_column': ['a', 'b', 'c', 'd', 'e']}
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert 'target_column' in df.columns
    assert df['target_column'].dtype == np.int8  # Assuming category codes are int8
    assert ax.get_title() == 'Histogram of target_column'
    assert ax.get_xlabel() == 'target_column'

def test_task_func_with_missing_column():
    data = {'other_column': [1, 2, 3, 4, 5]}
    with pytest.raises(ValueError) as excinfo:
        task_func(data, column_name='target_column')
    assert str(excinfo.value) == "Column 'target_column' not found in the DataFrame."

def test_task_func_with_empty_data():
    data = {}
    with pytest.raises(ValueError) as excinfo:
        task_func(data, column_name='target_column')
    assert str(excinfo.value) == "Column 'target_column' not found in the DataFrame."