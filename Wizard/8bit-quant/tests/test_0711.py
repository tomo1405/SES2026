python
import pandas as pd
import pytest
from sklearn.preprocessing import MinMaxScaler
from src_0711 import task_func

def test_task_func():
    # Test case 1: Test with valid data
    data_path = "data.csv"
    df = pd.read_csv(data_path)
    expected_df = df.copy()
    expected_df = expected_df.apply(lambda x: (x - x.min()) / (x.max() - x.min()), axis=0)
    actual_df = task_func(data_path)
    assert actual_df.equals(expected_df)

    # Test case 2: Test with invalid data (empty dataframe)
    data_path = "empty_data.csv"
    df = pd.read_csv(data_path)
    expected_df = df.copy()
    expected_df = expected_df.apply(lambda x: (x - x.min()) / (x.max() - x.min()), axis=0)
    actual_df = task_func(data_path)
    assert actual_df.equals(expected_df)

    # Test case 3: Test with invalid data (non-numeric columns)
    data_path = "non_numeric_data.csv"
    df = pd.read_csv(data_path)
    expected_df = df.copy()
    expected_df = expected_df.apply(lambda x: (x - x.min()) / (x.max() - x.min()), axis=0)
    actual_df = task_func(data_path)
    assert actual_df.equals(expected_df)