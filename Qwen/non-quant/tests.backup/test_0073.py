import pytest
from src_0073 import task_func
import pandas as pd
import numpy as np
import os
import ast

def test_task_func_no_csv_files(tmpdir):
    # Create a temporary directory with no CSV files
    result_df, hist = task_func(tmpdir)
    expected_df = pd.DataFrame({}, columns=['email', 'list', 'sum', 'mean', 'median'])
    assert result_df.equals(expected_df)
    assert hist is None

def test_task_func_single_csv_file(tmpdir):
    # Create a temporary directory with a single CSV file
    csv_content = "email,list\na,[1, 2, 3]\nb,[4, 5]"
    csv_file = tmpdir.join("test.csv")
    csv_file.write(csv_content)
    
    result_df, hist = task_func(tmpdir)
    expected_df = pd.DataFrame({
        "email": ["a", "b"],
        "list": [[1, 2, 3], [4, 5]],
        "sum": [6, 9],
        "mean": [2.0, 4.5],
        "median": [2.0, 4.5]
    })
    assert result_df.equals(expected_df)
    assert isinstance(hist, np.ndarray)

def test_task_func_multiple_csv_files(tmpdir):
    # Create a temporary directory with multiple CSV files
    csv_content_1 = "email,list\na,[1, 2, 3]\nb,[4, 5]"
    csv_content_2 = "email,list\nc,[6, 7, 8, 9]"
    csv_file_1 = tmpdir.join("file1.csv")
    csv_file_2 = tmpdir.join("file2.csv")
    csv_file_1.write(csv_content_1)
    csv_file_2.write(csv_content_2)
    
    result_df, hist = task_func(tmpdir)
    expected_df = pd.DataFrame({
        "email": ["c"],
        "list": [[6, 7, 8, 9]],
        "sum": [30],
        "mean": [7.5],
        "median": [7.5]
    })
    assert result_df.equals(expected_df)
    assert isinstance(hist, np.ndarray)

def test_task_func_empty_csv_file(tmpdir):
    # Create a temporary directory with an empty CSV file
    csv_content = ""
    csv_file = tmpdir.join("empty.csv")
    csv_file.write(csv_content)
    
    result_df, hist = task_func(tmpdir)
    expected_df = pd.DataFrame({}, columns=['email', 'list', 'sum', 'mean', 'median'])
    assert result_df.equals(expected_df)
    assert hist is None

def test_task_func_invalid_csv_content(tmpdir):
    # Create a temporary directory with a CSV file containing invalid data
    csv_content = "email,list\na,not_a_list"
    csv_file = tmpdir.join("invalid.csv")
    csv_file.write(csv_content)
    
    result_df, hist = task_func(tmpdir)
    expected_df = pd.DataFrame({}, columns=['email', 'list', 'sum', 'mean', 'median'])
    assert result_df.equals(expected_df)
    assert hist is None