python
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt
import pytest

def task_func(df):
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty pandas DataFrame.")

    last_col = df.columns[-1]
    imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
    df[last_col] = imp_mean.fit_transform(df[last_col].values.reshape(-1, 1))

    fig, ax = plt.subplots()
    sns.boxplot(x=df[last_col], ax=ax)
    ax.set_title('Boxplot of Last Column')
    ax.set_xlabel(last_col)
    return df, ax

def test_task_func():
    # Test case 1: Valid input
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    expected_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    expected_ax = None
    actual_df, actual_ax = task_func(df)
    assert expected_df.equals(actual_df)
    assert expected_ax == actual_ax

    # Test case 2: Empty input
    with pytest.raises(ValueError):
        task_func(pd.DataFrame())

    # Test case 3: Non-dataframe input
    with pytest.raises(ValueError):
        task_func([1, 2, 3])

    # Test case 4: Input with missing values
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, np.nan], 'C': [7, 8, 9]})
    expected_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 5], 'C': [7, 8, 9]})
    expected_ax = None
    actual_df, actual_ax = task_func(df)
    assert expected_df.equals(actual_df)
    assert expected_ax == actual_ax