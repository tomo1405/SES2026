import pytest
from src_0876 import task_func
import pandas as pd
import numpy as np

def test_task_func_no_fill():
    data = [
        {'Name': 'Alice', 'Age': 25, 'Occupation': 'Engineer'},
        {'Name': 'Bob', 'Age': np.nan, 'Occupation': 'Designer'}
    ]
    expected_df = pd.DataFrame(data, columns=['Name', 'Age', 'Occupation'])
    result_df = task_func(data)
    assert result_df.equals(expected_df)

def test_task_func_with_fill():
    data = [
        {'Name': 'Alice', 'Age': 25, 'Occupation': 'Engineer'},
        {'Name': 'Bob', 'Age': np.nan, 'Occupation': 'Designer'}
    ]
    expected_df = pd.DataFrame(data, columns=['Name', 'Age', 'Occupation'])
    expected_df['Age'] = expected_df['Age'].fillna(50)  # Assuming 50 is within the default range (0, 100)
    result_df = task_func(data, fill_missing=True)
    assert result_df.equals(expected_df)

def test_task_func_custom_columns():
    data = [
        {'Name': 'Alice', 'Age': 25, 'Occupation': 'Engineer'},
        {'Name': 'Bob', 'Age': np.nan, 'Occupation': 'Designer'}
    ]
    columns = ['Name', 'Age', 'Role']
    expected_df = pd.DataFrame(data, columns=columns)
    result_df = task_func(data, columns=columns)
    assert result_df.equals(expected_df)

def test_task_func_custom_seed():
    data = [
        {'Name': 'Alice', 'Age': 25, 'Occupation': 'Engineer'},
        {'Name': 'Bob', 'Age': np.nan, 'Occupation': 'Designer'}
    ]
    seed = 42
    expected_df = pd.DataFrame(data, columns=['Name', 'Age', 'Occupation'])
    expected_df['Age'] = expected_df['Age'].fillna(50)  # Assuming 50 is within the default range (0, 100)
    result_df = task_func(data, fill_missing=True, seed=seed)
    assert result_df.equals(expected_df)

def test_task_func_custom_num_range():
    data = [
        {'Name': 'Alice', 'Age': 25, 'Occupation': 'Engineer'},
        {'Name': 'Bob', 'Age': np.nan, 'Occupation': 'Designer'}
    ]
    num_range = (50, 150)
    expected_df = pd.DataFrame(data, columns=['Name', 'Age', 'Occupation'])
    expected_df['Age'] = expected_df['Age'].fillna(100)  # Assuming 100 is within the custom range (50, 150)
    result_df = task_func(data, fill_missing=True, num_range=num_range)
    assert result_df.equals(expected_df)