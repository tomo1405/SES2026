import re
import pandas as pd
import numpy as np
from src_0644 import task_func

# Constants
DATA_PATTERN = r'>\d+\.\d+<'

# Sample input data
data = {
    'col1': ['>1.2<', '2.3', '3.4', '4.5', '5.6'],
    'col2': ['>2.3<', '3.4', '4.5', '5.6', '6.7'],
    'col3': ['>3.4<', '4.5', '5.6', '6.7', '7.8'],
    'col4': ['>4.5<', '5.6', '6.7', '7.8', '8.9'],
    'col5': ['>5.6<', '6.7', '7.8', '8.9', '9.0']
}

# Create a sample pandas DataFrame
df = pd.DataFrame(data)

# Test the function with the sample input data
def test_task_func():
    result = task_func(df)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == df.shape
    for col in df.columns:
        for value, expected in zip(result[col], df[col]):
            if pd.notnull(value):
                assert re.search(DATA_PATTERN, value)
            else:
                assert pd.isnull(expected)

# Test the function with an empty DataFrame
def test_task_func_empty():
    empty_df = pd.DataFrame()
    result = task_func(empty_df)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == empty_df.shape

# Test the function with a DataFrame containing only null values
def test_task_func_all_null():
    all_null_df = pd.DataFrame(columns=['col1', 'col2', 'col3', 'col4', 'col5'])
    result = task_func(all_null_df)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == all_null_df.shape
    for col in all_null_df.columns:
        for value in result[col]:
            assert pd.isnull(value)