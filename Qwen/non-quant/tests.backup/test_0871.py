import pytest
from src_0871 import task_func
import pandas as pd
import numpy as np

def test_task_func_default_input():
    expected_df = pd.DataFrame({
        'Mean Value': [3.0, 3.6, 4.2, 4.8, 5.4]
    }, index=['Position 0', 'Position 1', 'Position 2', 'Position 3', 'Position 4'])
    
    result_df = task_func()
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_empty_input():
    expected_df = pd.DataFrame({
        'Mean Value': [np.nan, np.nan, np.nan]
    }, index=['Position 0', 'Position 1', 'Position 2'])
    
    result_df = task_func([(), (), ()])
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_mixed_data_types():
    data_list = [('a', 1, 'x'), ('b', 2, 3.2), ('c', 3, 'y'), ('d', 4, 5.4), ('e', 5, 'z')]
    expected_df = pd.DataFrame({
        'Mean Value': [3.0, 4.3]
    }, index=['Position 0', 'Position 1'])
    
    result_df = task_func(data_list)
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_single_column():
    data_list = [('a', 1), ('b', 2), ('c', 3)]
    expected_df = pd.DataFrame({
        'Mean Value': [2.0]
    }, index=['Position 0'])
    
    result_df = task_func(data_list)
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_all_non_numeric():
    data_list = [('a', 'x'), ('b', 'y'), ('c', 'z')]
    expected_df = pd.DataFrame({
        'Mean Value': [np.nan, np.nan]
    }, index=['Position 0', 'Position 1'])
    
    result_df = task_func(data_list)
    pd.testing.assert_frame_equal(result_df, expected_df)