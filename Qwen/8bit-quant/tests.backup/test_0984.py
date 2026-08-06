import pytest
from src_0984 import task_func
import pandas as pd
import numpy as np

def test_task_func_empty_dataframe():
    df = pd.DataFrame()
    with pytest.raises(ValueError, match="DataFrame is empty. Non-empty DataFrame required."):
        task_func(df)

def test_task_func_non_numeric_data():
    df = pd.DataFrame({'A': [1, 2, 'a'], 'B': [4, 5, 6]})
    with pytest.raises(TypeError, match="DataFrame contains non-numeric data. Only numeric data types are supported."):
        task_func(df)

def test_task_func_valid_dataframe():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    covariance_df, pair_plot = task_func(df)
    assert isinstance(covariance_df, pd.DataFrame)
    assert isinstance(pair_plot, sns.axisgrid.PairGrid)

def test_task_func_single_column_dataframe():
    df = pd.DataFrame({'A': [1, 2, 3]})
    covariance_df, pair_plot = task_func(df)
    assert isinstance(covariance_df, pd.DataFrame)
    assert isinstance(pair_plot, sns.axisgrid.PairGrid)

def test_task_func_all_zero_variance():
    df = pd.DataFrame({'A': [0, 0, 0], 'B': [0, 0, 0]})
    covariance_df, pair_plot = task_func(df)
    assert (covariance_df == 0).all().all()
    assert isinstance(pair_plot, sns.axisgrid.PairGrid)