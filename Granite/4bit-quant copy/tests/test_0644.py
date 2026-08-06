import re
import pandas as pd
import numpy as np
from src_0644 import task_func

# Constants
DATA_PATTERN = r'>\d+\.\d+<'

# Test data
test_dataframe = pd.DataFrame({
    'col1': ['>1.2<', '2.3', '3.4>', '4.5<', np.nan, '6.7>'],
    'col2': ['>2.4<', '3.5', '4.6>', '5.7<', '6.8>', '7.9>']
})

# Expected results
expected_result = pd.DataFrame({
    'col1': [1.2, 2.3, 3.4, 4.5, np.nan, 6.7],
    'col2': [2.4, 3.5, 4.6, 5.7, 6.8, 7.9]
})

def test_task_func():
    result = task_func(test_dataframe)
    assert result.equals(expected_result)

def test_task_func_with_null_values():
    test_dataframe_with_nulls = test_dataframe.copy()
    test_dataframe_with_nulls.loc[0, 'col1'] = np.nan
    expected_result_with_nulls = expected_result.copy()
    expected_result_with_nulls.loc[0, 'col1'] = np.nan
    result_with_nulls = task_func(test_dataframe_with_nulls)
    assert result_with_nulls.equals(expected_result_with_nulls)

def test_task_func_with_invalid_data():
    test_dataframe_with_invalid_data = test_dataframe.copy()
    test_dataframe_with_invalid_data.loc[0, 'col1'] = 'abc'
    expected_result_with_invalid_data = expected_result.copy()
    expected_result_with_invalid_data.loc[0, 'col1'] = np.nan
    result_with_invalid_data = task_func(test_dataframe_with_invalid_data)
    assert result_with_invalid_data.equals(expected_result_with_invalid_data)