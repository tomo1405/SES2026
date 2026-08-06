import pytest
from src_0652 import task_func
import pandas as pd

def test_task_func_with_non_empty_dataframe():
    df = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [1, 1, 2, 3],
        'C': [4, 3, 2, 1]
    })
    target_value = '1'
    counts, ax = task_func(df, target_value)
    
    expected_counts = pd.Series({'A': 1, 'B': 2, 'C': 1})
    assert counts.equals(expected_counts)
    assert ax is not None

def test_task_func_with_empty_dataframe():
    df = pd.DataFrame()
    target_value = '1'
    counts, ax = task_func(df, target_value)
    
    expected_counts = pd.Series(dtype=int)
    assert counts.equals(expected_counts)
    assert ax is None

def test_task_func_with_all_values_equal_to_target():
    df = pd.DataFrame({
        'A': ['1', '1', '1'],
        'B': ['1', '1', '1']
    })
    target_value = '1'
    counts, ax = task_func(df, target_value)
    
    expected_counts = pd.Series({'A': 3, 'B': 3})
    assert counts.equals(expected_counts)
    assert ax is not None

def test_task_func_with_no_values_equal_to_target():
    df = pd.DataFrame({
        'A': ['2', '3', '4'],
        'B': ['5', '6', '7']
    })
    target_value = '1'
    counts, ax = task_func(df, target_value)
    
    expected_counts = pd.Series({'A': 0, 'B': 0})
    assert counts.equals(expected_counts)
    assert ax is not None

def test_task_func_with_mixed_data_types():
    df = pd.DataFrame({
        'A': [1, '2', 3],
        'B': ['1', 1, '1']
    })
    target_value = '1'
    counts, ax = task_func(df, target_value)
    
    expected_counts = pd.Series({'A': 1, 'B': 2})
    assert counts.equals(expected_counts)
    assert ax is not None