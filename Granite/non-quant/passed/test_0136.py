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

    # Test case 3: Input is a pandas DataFrame with missing values
    df = pd.DataFrame({'A': [1, 2, np.nan, 4, 5], 'B': [np.nan, 2, 3, 4, 5]})
    expected_df = pd.DataFrame({'A': [1.0, 2.0, 3.0, 4.0, 5.0], 'B': [3.0, 2.0, 3.0, 4.0, 5.0]})
    _, ax = task_func(df)
    assert df.equals(expected_df)
    assert ax.get_title() == 'Boxplot of Last Column'
    assert ax.get_xlabel() == last_col

    # Test case 4: Input is a pandas DataFrame with no missing values
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]})
    expected_df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]})
    _, ax = task_func(df)
    assert df.equals(expected_df)
    assert ax.get_title() == 'Boxplot of Last Column'
    assert ax.get_xlabel() == last_col