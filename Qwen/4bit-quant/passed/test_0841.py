import pytest
from src_0841 import task_func
import pandas as pd
import os

def test_task_func_output():
    # Define test parameters
    file_path = 'test_output.csv'
    num_rows = 10
    data_dimensions = 3
    random_seed = 42

    # Call the function under test
    result = task_func(file_path, num_rows, data_dimensions, random_seed)

    # Assert that the returned file path is correct
    assert result == file_path

    # Read the generated CSV file
    df = pd.read_csv(file_path)

    # Assert that the DataFrame has the correct number of rows and columns
    assert len(df) == num_rows
    assert len(df.columns) == data_dimensions

    # Assert that the column names are correct
    expected_columns = [f'Feature_{i + 1}' for i in range(data_dimensions)]
    assert list(df.columns) == expected_columns

    # Clean up: remove the generated file
    os.remove(file_path)

def test_task_func_randomness():
    # Define test parameters
    file_path = 'test_randomness.csv'
    num_rows = 5
    data_dimensions = 2
    random_seed = 0

    # Call the function under test with the same random seed
    task_func(file_path, num_rows, data_dimensions, random_seed)
    df1 = pd.read_csv(file_path)

    # Call the function again with the same parameters and random seed
    task_func(file_path, num_rows, data_dimensions, random_seed)
    df2 = pd.read_csv(file_path)

    # Assert that the DataFrames are identical
    assert df1.equals(df2)

    # Clean up: remove the generated file
    os.remove(file_path)