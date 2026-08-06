import pytest
from src_0348 import task_func
import pandas as pd
import numpy as np

def test_task_func_no_matches():
    data = {'hex_column': ['no hex here', 'still no hex']}
    df = pd.DataFrame(data)
    result = task_func(df, 'hex_column')
    assert result.empty

def test_task_func_single_match():
    data = {'hex_column': ['1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7a8b9c0d1e2f3']}
    df = pd.DataFrame(data)
    result = task_func(df, 'hex_column')
    expected = pd.Series({data['hex_column'][0]: 1})
    pd.testing.assert_series_equal(result, expected)

def test_task_func_multiple_matches():
    data = {'hex_column': ['1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7a8b9c0d1e2f3', 
                           '1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7a8b9c0d1e2f3', 
                           'abcd1234abcd1234']}
    df = pd.DataFrame(data)
    result = task_func(df, 'hex_column')
    expected = pd.Series({'1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7a8b9c0d1e2f3': 2, 
                          'abcd1234abcd1234': 1})
    pd.testing.assert_series_equal(result, expected)

def test_task_func_empty_column():
    data = {'hex_column': [None, '', np.nan]}
    df = pd.DataFrame(data)
    result = task_func(df, 'hex_column')
    assert result.empty

def test_task_func_mixed_data_types():
    data = {'hex_column': ['1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7a8b9c0d1e2f3', 
                           12345, 
                           'not a hex', 
                           '6f1234567890abcdef1234567890abcdef']}
    df = pd.DataFrame(data)
    result = task_func(df, 'hex_column')
    expected = pd.Series({'1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7a8b9c0d1e2f3': 1, 
                          '6f1234567890abcdef1234567890abcdef': 1})
    pd.testing.assert_series_equal(result, expected)