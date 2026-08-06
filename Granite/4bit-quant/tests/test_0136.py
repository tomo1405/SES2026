import pytest
from src_0136 import task_func
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt

def test_task_func():
    # Test case 1: Input is not a pandas DataFrame
    with pytest.raises(ValueError) as excinfo:
        task_func(np.array([1, 2, 3]))
    assert "Input must be a non-empty pandas DataFrame." in str(excinfo.value)

    # Test case 2: Input is an empty pandas DataFrame
    with pytest.raises(ValueError) as excinfo:
        task_func(pd.DataFrame())
    assert "Input must be a non-empty pandas DataFrame." in str(excinfo.value)

    # Test case 3: Input is a pandas DataFrame with missing values
    df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, 5, 6]})
    expected_df = pd.DataFrame({'A': [1, 2, 1.5], 'B': [4, 5, 6]})
    expected_ax_title = 'Boxplot of Last Column'
    expected_ax_xlabel = df.columns[-1]
    df_actual, ax_actual = task_func(df)
    assert df_actual.equals(expected_df)
    assert ax_actual.get_title() == expected_ax_title
    assert ax_actual.get_xlabel() == expected_ax_xlabel