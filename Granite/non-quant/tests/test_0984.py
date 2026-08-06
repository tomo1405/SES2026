import pytest
from src_0984 import task_func
import seaborn as sns
import numpy as np
import pandas as pd

def test_task_func_df_empty():
    df = pd.DataFrame()
    with pytest.raises(ValueError) as exc_info:
        task_func(df)
    assert "DataFrame is empty. Non-empty DataFrame required." in str(exc_info.value)

def test_task_func_df_non_numeric():
    df = pd.DataFrame({'A': ['a', 'b'], 'B': [1, 2]})
    with pytest.raises(TypeError) as exc_info:
        task_func(df)
    assert "DataFrame contains non-numeric data. Only numeric data types are supported." in str(exc_info.value)

def test_task_func_df_numeric():
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    covariance_df, pair_plot = task_func(df)
    assert isinstance(covariance_df, pd.DataFrame)
    assert isinstance(pair_plot, sns.axisgrid.PairGrid)