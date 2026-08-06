import json
import numpy as np
import pandas as pd
import pytest
from src_0708 import task_func

def test_task_func():
    # Create a sample DataFrame with an 'IntCol' column
    df = pd.DataFrame({'IntCol': [1, 10, 100, 1000]})

    # Call the function and store the result
    result = task_func(df)

    # Check if the 'IntCol' column has been modified
    expected_int_col = np.log10(df['IntCol'])
    assert np.array_equal(result['IntCol'], expected_int_col)

    # Check if the 'IntCol' column has been written to a JSON file
    with open('IntCol.json', 'r') as json_file:
        int_col_list = json.load(json_file)
    assert np.array_equal(int_col_list, expected_int_col.tolist())

    # Check if the function has returned the modified DataFrame
    assert result.equals(df)

def test_task_func_with_null_values():
    # Create a sample DataFrame with an 'IntCol' column and null values
    df = pd.DataFrame({'IntCol': [1, None, 10, np.nan]})

    # Call the function and store the result
    result = task_func(df)

    # Check if the 'IntCol' column has been modified
    expected_int_col = np.log10(df['IntCol'].dropna())
    assert np.array_equal(result['IntCol'], expected_int_col)

    # Check if the 'IntCol' column has been written to a JSON file
    with open('IntCol.json', 'r') as json_file:
        int_col_list = json.load(json_file)
    assert np.array_equal(int_col_list, expected_int_col.tolist())

    # Check if the function has returned the modified DataFrame
    assert result.equals(df)