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
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
    assert task_func(df) == 0.0

    # Test case 2: Invalid input (empty DataFrame)
    with pytest.raises(ValueError):
        task_func(pd.DataFrame())

    # Test case 3: Invalid input (non-DataFrame input)
    with pytest.raises(ValueError):
        task_func([1, 2, 3])