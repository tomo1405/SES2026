import pytest
from src_0244 import task_func

def test_task_func():
    # Test that the function returns a DataFrame with the correct number of rows
    n_data_points = 10
    data_df = task_func(n_data_points)
    assert len(data_df) == n_data_points

    # Test that the function returns a DataFrame with the correct column names
    assert data_df.columns.tolist() == ['Value']

    # Test that the function returns a DataFrame with the correct data types
    assert data_df['Value'].dtype == float

    # Test that the function returns a DataFrame with the correct data values
    expected_data = [round(random.uniform(MIN_VALUE, MAX_VALUE), 3) for _ in range(n_data_points)]
    assert data_df['Value'].tolist() == expected_data

def test_task_func_with_zero_data_points():
    # Test that the function returns an empty DataFrame when n_data_points is 0
    n_data_points = 0
    data_df = task_func(n_data_points)
    assert len(data_df) == 0

    # Test that the function returns a DataFrame with the correct column names
    assert data_df.columns.tolist() == ['Value']

    # Test that the function returns a DataFrame with the correct data types
    assert data_df['Value'].dtype == float

    # Test that the function returns a DataFrame with the correct data values
    expected_data = []
    assert data_df['Value'].tolist() == expected_data