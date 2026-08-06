import pytest
from src_0226 import task_func
import pandas as pd

# Test cases
def test_task_func_basic():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    dct = {1: 10, 2: 20}
    expected_df = pd.DataFrame({'A': [10, 20, 3], 'B': [4, 5, 6]})
    result_df = task_func(df, dct)
    assert result_df.equals(expected_df)

def test_task_func_with_columns():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    dct = {1: 10, 2: 20}
    columns = ['A']
    expected_df = pd.DataFrame({'A': [10, 20, 3], 'B': [4, 5, 6]})
    result_df = task_func(df, dct, columns=columns)
    assert result_df.equals(expected_df)

def test_task_func_no_replacement():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    dct = {7: 10, 8: 20}
    expected_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    result_df = task_func(df, dct)
    assert result_df.equals(expected_df)

def test_task_func_invalid_df():
    with pytest.raises(ValueError):
        task_func([1, 2, 3], {})

def test_task_func_plot_histograms():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    dct = {1: 10, 2: 20}
    columns = ['A']
    task_func(df, dct, columns=columns, plot_histograms=True)
    # Since we're not capturing plots, we can't assert anything here.
    # In practice, you might use a library like `matplotlib.testing.decorators` to check plots.

def test_task_func_no_columns():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    dct = {1: 10, 2: 20}
    expected_df = pd.DataFrame({'A': [10, 20, 3], 'B': [4, 5, 6]})
    result_df = task_func(df, dct, plot_histograms=True)
    assert result_df.equals(expected_df)