python
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
    # Test case 1: Test with empty DataFrame
    with pytest.raises(ValueError):
        task_func(pd.DataFrame())

    # Test case 2: Test with non-numeric DataFrame
    with pytest.raises(TypeError):
        task_func(pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']}))

    # Test case 3: Test with valid DataFrame
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    covariance_df, pair_plot = task_func(df)
    assert isinstance(covariance_df, pd.DataFrame)
    assert isinstance(pair_plot, sns.axisgrid.PairGrid)