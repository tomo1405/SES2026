python
import pandas as pd
from random import uniform
import pytest

def task_func(n_data_points=1000, min_value=0.0, max_value=10.0, column_name='Value'):

    data = [round(uniform(min_value, max_value), 3) for _ in range(n_data_points)]
    data_df = pd.DataFrame(data, columns=[column_name])

    return data_df

def test_task_func():
    data_df = task_func()
    assert isinstance(data_df, pd.DataFrame)
    assert data_df.shape[0] == 1000
    assert data_df.shape[1] == 1
    assert data_df.columns[0] == 'Value'
    assert all(data_df['Value'] >= 0.0)
    assert all(data_df['Value'] <= 10.0)