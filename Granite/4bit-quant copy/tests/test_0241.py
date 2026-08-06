import pandas as pd
from random import uniform
from src_0241 import task_func
import pytest

def test_task_func():
    # Test with default arguments
    result_df = task_func()
    assert isinstance(result_df, pd.DataFrame)
    assert len(result_df) == 1000
    assert 'Value' in result_df.columns
    assert result_df['Value'].min() >= 0.0
    assert result_df['Value'].max() <= 10.0

    # Test with custom arguments
    result_df = task_func(n_data_points=100, min_value=1.0, max_value=5.0, column_name='Custom')
    assert isinstance(result_df, pd.DataFrame)
    assert len(result_df) == 100
    assert 'Custom' in result_df.columns
    assert result_df['Custom'].min() >= 1.0
    assert result_df['Custom'].max() <= 5.0