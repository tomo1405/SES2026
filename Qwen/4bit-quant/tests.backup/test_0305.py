import pytest
from src_0305 import task_func
import pandas as pd
import numpy as np

def test_task_func_empty_df():
    df = pd.DataFrame(columns=['Date', 'Value'])
    result = task_func(df)
    assert result == (0, 0)

def test_task_func_non_empty_df():
    data = {
        'Date': ['2020-01-01', '2020-01-02', '2020-01-03'],
        'Value': [[1, 2], [3, 4], [5, 6]]
    }
    df = pd.DataFrame(data)
    explained_variance_ratio, ax = task_func(df)
    
    assert isinstance(explained_variance_ratio, np.ndarray)
    assert len(explained_variance_ratio) > 0
    assert isinstance(ax, plt.Axes)

def test_task_func_single_row_df():
    data = {
        'Date': ['2020-01-01'],
        'Value': [[1, 2]]
    }
    df = pd.DataFrame(data)
    explained_variance_ratio, ax = task_func(df)
    
    assert isinstance(explained_variance_ratio, np.ndarray)
    assert len(exploded_variance_ratio) > 0
    assert isinstance(ax, plt.Axes)

def test_task_func_with_different_value_lengths():
    data = {
        'Date': ['2020-01-01', '2020-01-02'],
        'Value': [[1, 2, 3], [4, 5]]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError):
        task_func(df)