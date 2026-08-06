import pandas as pd
from random import uniform
from src_0241 import task_func
import pytest

def test_task_func():
    # Test with default arguments
    result_df = task_func()
    assert isinstance(result_df, pd.DataFrame)
    assert len(result_df) == 1000
    assert result_df.columns[0] == 'Value'
    assert result_df.Value.min() >= 0.0
    assert result_df.Value.max() <= 10.0

    # Test with custom arguments
    n_data_points = 500
    min_value = 5.0
    max_value = 15.0
    column_name = 'MyValue'
    result_df = task_func(n_data_points, min_value, max_value, column_name)
    assert isinstance(result_df, pd.DataFrame)
    assert len(result_df) == n_data_points
    assert result_df.columns[0] == column_name
    assert result_df[column_name].min() >= min_value
    assert result_df[column_name].max() <= max_value