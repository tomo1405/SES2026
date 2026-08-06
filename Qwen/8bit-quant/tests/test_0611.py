import pytest
from src_0611 import task_func
import pandas as pd

def test_task_func_empty_df():
    df = pd.DataFrame(columns=['A', 'B', 'C', 'D', 'E'])
    tuples = [(1, 2, 3, 4, 5)]
    n_plots = 3
    
    result_df, plots = task_func(df, tuples, n_plots)
    
    assert result_df.equals(df)
    assert plots == []

def test_task_func_no_tuples():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9],
        'D': [10, 11, 12],
        'E': [13, 14, 15]
    })
    tuples = []
    n_plots = 2
    
    result_df, plots = task_func(df, tuples, n_plots)
    
    assert result_df.equals(df)
    assert len(plots) == n_plots

def test_task_func_with_tuples():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9],
        'D': [10, 11, 12],
        'E': [13, 14, 15]
    })
    tuples = [(1, 2, 3, 4, 5)]
    n_plots = 2
    
    result_df, plots = task_func(df, tuples, n_plots)
    
    assert not result_df.equals(df)
    assert len(plots) == n_plots

def test_task_func_no_plots():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9],
        'D': [10, 11, 12],
        'E': [13, 14, 15]
    })
    tuples = []
    n_plots = 0
    
    result_df, plots = task_func(df, tuples, n_plots)
    
    assert result_df.equals(df)
    assert plots == []

def test_task_func_all_rows_dropped():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9],
        'D': [10, 11, 12],
        'E': [13, 14, 15]
    })
    tuples = [(1, 2, 3, 4, 5), (2, 3, 4, 5, 6), (3, 4, 5, 6, 7)]
    n_plots = 2
    
    result_df, plots = task_func(df, tuples, n_plots)
    
    assert result_df.empty
    assert plots == []