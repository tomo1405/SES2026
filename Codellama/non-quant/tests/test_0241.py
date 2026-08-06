import pandas as pd
import pytest
from src_0241 import task_func


def test_task_func():
    # Test with default parameters
    data_df = task_func()
    assert isinstance(data_df, pd.DataFrame)
    assert data_df.shape == (1000, 1)
    assert data_df.columns.tolist() == ['Value']
    assert all(data_df['Value'] >= 0.0) and all(data_df['Value'] <= 10.0)

    # Test with custom parameters
    data_df = task_func(n_data_points=500, min_value=5.0, max_value=15.0, column_name='Value2')
    assert isinstance(data_df, pd.DataFrame)
    assert data_df.shape == (500, 1)
    assert data_df.columns.tolist() == ['Value2']
    assert all(data_df['Value2'] >= 5.0) and all(data_df['Value2'] <= 15.0)

    # Test with invalid parameters
    with pytest.raises(ValueError):
        task_func(n_data_points=-1)
    with pytest.raises(ValueError):
        task_func(min_value=10.0, max_value=5.0)
    with pytest.raises(ValueError):
        task_func(column_name='')