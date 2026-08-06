import pytest
from src_0841 import task_func
import pandas as pd
import os

def test_task_func_default_dimensions(tmpdir):
    # Create a temporary directory and file path
    temp_dir = tmpdir.mkdir("temp")
    file_path = str(temp_dir.join("test_file.csv"))

    # Call the function with default data_dimensions
    result = task_func(file_path, num_rows=10)

    # Check if the file was created
    assert os.path.exists(file_path)

    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Check if the DataFrame has the correct number of rows and columns
    assert len(df) == 10
    assert len(df.columns) == 5

    # Check if the column names are correct
    expected_columns = [f'Feature_{i + 1}' for i in range(5)]
    assert list(df.columns) == expected_columns

def test_task_func_custom_dimensions(tmpdir):
    # Create a temporary directory and file path
    temp_dir = tmpdir.mkdir("temp")
    file_path = str(temp_dir.join("test_file.csv"))

    # Call the function with custom data_dimensions
    result = task_func(file_path, num_rows=10, data_dimensions=3)

    # Check if the file was created
    assert os.path.exists(file_path)

    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Check if the DataFrame has the correct number of rows and columns
    assert len(df) == 10
    assert len(df.columns) == 3

    # Check if the column names are correct
    expected_columns = [f'Feature_{i + 1}' for i in range(3)]
    assert list(df.columns) == expected_columns

def test_task_func_random_seed(tmpdir):
    # Create a temporary directory and file path
    temp_dir = tmpdir.mkdir("temp")
    file_path = str(temp_dir.join("test_file.csv"))

    # Call the function with a specific random seed
    task_func(file_path, num_rows=10, random_seed=42)

    # Load the CSV file into a DataFrame
    df1 = pd.read_csv(file_path)

    # Call the function again with the same random seed
    task_func(file_path, num_rows=10, random_seed=42)

    # Load the CSV file into another DataFrame
    df2 = pd.read_csv(file_path)

    # Check if the DataFrames are identical
    assert df1.equals(df2)