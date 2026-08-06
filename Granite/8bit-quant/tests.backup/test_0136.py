import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt
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
import pytest

def test_task_func():
    # Test case 1: Input is not a pandas DataFrame
    with pytest.raises(ValueError) as excinfo:
        task_func(np.array([[1, 2, 3], [4, 5, 6]]))
    assert "Input must be a non-empty pandas DataFrame." in str(excinfo.value)

    # Test case 2: Input is an empty pandas DataFrame
    with pytest.raises(ValueError) as excinfo:
        task_func(pd.DataFrame())
    assert "Input must be a non-empty pandas DataFrame." in str(excinfo.value)

    # Test case 3: Input is a pandas DataFrame with no missing values
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    result_df, result_ax = task_func(df)
    expected_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    expected_ax = None
    assert result_df.equals(expected_df) and result_ax == expected_ax

    # Test case 4: Input is a pandas DataFrame with missing values
    df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, 5, 6]})
    result_df, result_ax = task_func(df)
    expected_df = pd.DataFrame({'A': [1, 2, 2.5], 'B': [4, 5, 6]})
    expected_ax = None
    assert result_df.equals(expected_df) and result_ax == expected_ax