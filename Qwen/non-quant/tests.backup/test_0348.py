import pytest
from src_0348 import task_func
import pandas as pd

def test_task_func_no_matches():
    df = pd.DataFrame({ 'data': ['no matches here', 'or here'] })
    result = task_func(df, 'data')
    assert result.empty

def test_task_func_single_match():
    df = pd.DataFrame({ 'data': ['1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7a8b9c0d'] })
    result = task_func(df, 'data')
    assert result['1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7a8b9c0d'] == 1

def test_task_func_multiple_matches():
    df = pd.DataFrame({ 'data': ['1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7a8b9c0d 1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7a8b9c0d', 'another match 1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7a8b9c0d'] })
    result = task_func(df, 'data')
    assert result['1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7a8b9c0d'] == 3

def test_task_func_case_insensitivity():
    df = pd.DataFrame({ 'data': ['1A2B3C4D5E6F7G8H9I0J1K2L3M4N5O6P7Q8R9S0T1U2V3W4X5Y6Z7A8B9C0D', '1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7a8b9c0d'] })
    result = task_func(df, 'data')
    assert result['1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7a8b9c0d'] == 2

def test_task_func_empty_string():
    df = pd.DataFrame({ 'data': [''] })
    result = task_func(df, 'data')
    assert result.empty

def test_task_func_nonexistent_column():
    df = pd.DataFrame({ 'data': ['1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7a8b9c0d'] })
    with pytest.raises(KeyError):
        task_func(df, 'nonexistent_column')