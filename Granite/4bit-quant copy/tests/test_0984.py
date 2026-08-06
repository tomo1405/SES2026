import pytest
import seaborn as sns
import numpy as np

def task_func(df):
    if df.empty:
        raise ValueError("DataFrame is empty. Non-empty DataFrame required.")
    if not all(df.dtypes.apply(lambda x: np.issubdtype(x, np.number))):
        raise TypeError(
            "DataFrame contains non-numeric data. Only numeric data types are supported."
        )
    covariance_df = df.cov()
    pair_plot = sns.pairplot(df)

    return covariance_df, pair_plot

def test_task_func():
    import pandas as pd

    # Test case 1: Empty DataFrame
    df = pd.DataFrame()
    with pytest.raises(ValueError) as exc_info:
        task_func(df)
    assert "DataFrame is empty. Non-empty DataFrame required." in str(exc_info.value)

    # Test case 2: Non-numeric data
    df = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': [1, 2, 3]})
    with pytest.raises(TypeError) as exc_info:
        task_func(df)
    assert "DataFrame contains non-numeric data. Only numeric data types are supported." in str(exc_info.value)

    # Test case 3: Valid input
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    covariance_df, pair_plot = task_func(df)
    assert isinstance(covariance_df, pd.DataFrame)
    assert isinstance(pair_plot, sns.axisgrid.PairGrid)