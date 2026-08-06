import pandas as pd
import pytest
from src_0241 import task_func


def test_task_func():
    # Test with default arguments
    data_df = task_func()
    assert isinstance(data_df, pd.DataFrame)
    assert data_df.shape == (1000, 1)
    assert data_df.columns.tolist() == ['Value']
    assert all(data_df['Value'] >= 0) and all(data_df['Value'] <= 10)

    # Test with custom arguments
    data_df = task_func(n_data_points=500, min_value=5.0, max_value=15.0, column_name='Data')
    assert isinstance(data_df, pd.DataFrame)
    assert data_df.shape == (500, 1)
    assert data_df.columns.tolist() == ['Data']
    assert all(data_df['Data'] >= 5) and all(data_df['Data'] <= 15)

    # Test with invalid arguments
    with pytest.raises(ValueError):
        task_func(n_data_points=-10)
    with pytest.raises(ValueError):
        task_func(min_value=10.0, max_value=5.0)
    with pytest.raises(ValueError):
        task_func(column_name=1)