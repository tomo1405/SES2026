import pytest
from src_0876 import task_func
import pandas as pd
import numpy as np

def test_task_func_basic():
    data = [['Alice', 25, 'Engineer'], ['Bob', np.nan, 'Doctor']]
    expected_columns = ['Name', 'Age', 'Occupation']
    result_df = task_func(data)
    assert list(result_df.columns) == expected_columns
    assert result_df.shape == (2, 3)

def test_task_func_fill_missing():
    data = [['Alice', 25, 'Engineer'], ['Bob', np.nan, 'Doctor']]
    result_df = task_func(data, fill_missing=True, seed=42)
    assert result_df['Age'][1] == 60  # Expected value based on seed 42 and range (0, 100)

def test_task_func_no_fill_missing():
    data = [['Alice', 25, 'Engineer'], ['Bob', np.nan, 'Doctor']]
    result_df = task_func(data, fill_missing=False)
    assert pd.isnull(result_df['Age'][1])

def test_task_func_custom_columns():
    data = [['Alice', 25, 'Engineer'], ['Bob', 30, 'Doctor']]
    custom_columns = ['Name', 'Age', 'Job']
    result_df = task_func(data, columns=custom_columns)
    assert list(result_df.columns) == custom_columns

def test_task_func_empty_data():
    data = []
    result_df = task_func(data)
    assert result_df.empty

def test_task_func_non_numeric_fill():
    data = [['Alice', 25, 'Engineer'], ['Bob', np.nan, 'Doctor']]
    result_df = task_func(data, fill_missing=True, seed=42)
    assert result_df['Occupation'][1] == 'Doctor'  # Non-numeric columns should remain unchanged