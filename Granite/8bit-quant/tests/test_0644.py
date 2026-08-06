import re
import pandas as pd
import numpy as np
from src_0644 import task_func

# Constants
DATA_PATTERN = r'>\d+\.\d+<'

# Sample input data
data = {
    'col1': ['>1.2<', '2.3', '3.4>', '4.5<', '5.6>'],
    'col2': ['>1.2<', '2.3', np.nan, '4.5<', '5.6>'],
    'col3': ['>1.2<', '2.3', '3.4>', np.nan, '5.6>'],
    'col4': ['>1.2<', '2.3', '3.4>', '4.5<', np.nan]
}

# Create a sample pandas DataFrame
df = pd.DataFrame(data)

# Expected output data
expected_output = {
    'col1': [1.2, 2.3, 3.4, 4.5, 5.6],
    'col2': [1.2, 2.3, np.nan, 4.5, 5.6],
    'col3': [1.2, 2.3, 3.4, np.nan, 5.6],
    'col4': [1.2, 2.3, 3.4, 4.5, np.nan]
}

# Create a sample expected pandas DataFrame
expected_df = pd.DataFrame(expected_output)

def test_task_func():
    # Test the function with the sample input data
    output_df = task_func(df, data_pattern=DATA_PATTERN)
    
    # Check if the output DataFrame matches the expected DataFrame
    assert output_df.equals(expected_df)

def test_task_func_with_nan():
    # Test the function with a NaN value in the input data
    df['col1'][2] = np.nan
    expected_df['col1'][2] = np.nan
    output_df = task_func(df, data_pattern=DATA_PATTERN)
    assert output_df.equals(expected_df)

def test_task_func_with_no_match():
    # Test the function with input data that does not match the data pattern
    df['col5'] = ['abc', 'def', 'ghi', 'jkl', 'mno']
    expected_df['col5'] = [np.nan, np.nan, np.nan, np.nan, np.nan]
    output_df = task_func(df, data_pattern=DATA_PATTERN)
    assert output_df.equals(expected_df)