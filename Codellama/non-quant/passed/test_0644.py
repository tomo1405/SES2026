import pytest
from src_0644 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    # Test case 1: Test with a valid dataframe
    dataframe = pd.DataFrame({'A': ['>1.23<', '>4.56<', '>7.89<'], 'B': ['>10.11<', '>12.13<', '>14.15<']})
    expected_output = pd.DataFrame({'A': [1.23, 4.56, 7.89], 'B': [10.11, 12.13, 14.15]})
    output = task_func(dataframe)
    pd.testing.assert_frame_equal(output, expected_output)

    # Test case 2: Test with a dataframe with invalid data
    dataframe = pd.DataFrame({'A': ['>1.23<', '>4.56<', '>7.89<'], 'B': ['>10.11<', '>12.13<', '>14.15<']})
    dataframe.iloc[0, 0] = 'invalid data'
    expected_output = pd.DataFrame({'A': [np.nan, 4.56, 7.89], 'B': [10.11, 12.13, 14.15]})
    output = task_func(dataframe)
    pd.testing.assert_frame_equal(output, expected_output)

    # Test case 3: Test with a dataframe with no data
    dataframe = pd.DataFrame({'A': [], 'B': []})
    expected_output = pd.DataFrame({'A': [], 'B': []})
    output = task_func(dataframe)
    pd.testing.assert_frame_equal(output, expected_output)