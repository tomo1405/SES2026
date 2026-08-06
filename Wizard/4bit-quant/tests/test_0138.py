python
import pandas as pd
import pytest
from scipy.stats import skew

def task_func(df):
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty pandas DataFrame.")

    last_col = df.columns[-1]
    skewness = skew(df[last_col].dropna())  # dropna() to handle NaN values

    return skewness

def test_task_func():
    # Test case 1: Valid input
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    assert task_func(df) == 0.0

    # Test case 2: Invalid input (empty DataFrame)
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df)

    # Test case 3: Invalid input (not a DataFrame)
    df = [1, 2, 3]
    with pytest.raises(ValueError):
        task_func(df)

    # Test case 4: Invalid input (last column contains NaN values)
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, None]})
    with pytest.raises(ValueError):
        task_func(df)