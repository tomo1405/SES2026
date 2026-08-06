import pytest
from src_0704 import task_func
import numpy as np
import pandas as pd

def test_task_func_with_valid_data():
    data = [[1, 2], [2, 2], [2, 3], [8, 7], [8, 8], [25, 80]]
    cols = ['A', 'B']
    result_df = task_func(data, cols)
    
    assert isinstance(result_df, pd.DataFrame)
    assert 'Cluster' in result_df.columns
    assert len(result_df) == len(data)

def test_task_func_with_empty_data():
    data = []
    cols = ['A', 'B']
    result_df = task_func(data, cols)
    
    assert isinstance(result_df, pd.DataFrame)
    assert 'Cluster' in result_df.columns
    assert result_df.empty

def test_task_func_with_single_row_data():
    data = [[1, 2]]
    cols = ['A', 'B']
    result_df = task_func(data, cols)
    
    assert isinstance(result_df, pd.DataFrame)
    assert 'Cluster' in result_df.columns
    assert len(result_df) == len(data)

def test_task_func_with_identical_rows():
    data = [[1, 2], [1, 2], [1, 2]]
    cols = ['A', 'B']
    result_df = task_func(data, cols)
    
    assert isinstance(result_df, pd.DataFrame)
    assert 'Cluster' in result_df.columns
    assert len(result_df) == len(data)

def test_task_func_with_different_dimensions():
    data = [[1, 2], [2, 2, 3]]  # Second row has different dimensions
    cols = ['A', 'B']
    with pytest.raises(ValueError):
        task_func(data, cols)