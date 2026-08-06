python
import pandas as pd
from random import uniform
import pytest

def task_func(n_data_points=1000, min_value=0.0, max_value=10.0, column_name='Value'):

    data = [round(uniform(min_value, max_value), 3) for _ in range(n_data_points)]
    data_df = pd.DataFrame(data, columns=[column_name])

    return data_df

def test_task_func():
    # Test default values
    data_df = task_func()
    assert len(data_df) == 1000
    assert data_df.columns[0] == 'Value'
    assert data_df['Value'].min() >= 0.0
    assert data_df['Value'].max() <= 10.0

    # Test custom values
    data_df = task_func(n_data_points=500, min_value=5.0, max_value=15.0, column_name='Custom')
    assert len(data_df) == 500
    assert data_df.columns[0] == 'Custom'
    assert data_df['Custom'].min() >= 5.0
    assert data_df['Custom'].max() <= 15.0