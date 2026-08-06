import pytest
from src_0136 import task_func
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt

def test_task_func_input_validation():
    with pytest.raises(ValueError, match="Input must be a non-empty pandas DataFrame."):
        task_func(None)
    with pytest.raises(ValueError, match="Input must be a non-empty pandas DataFrame."):
        task_func(pd.DataFrame())

def test_task_func_imputation():
    df = pd.DataFrame({
        'A': [1, 2, np.nan],
        'B': [4, np.nan, 6]
    })
    expected_df = pd.DataFrame({
        'A': [1, 2, 1.5],
        'B': [4, 5, 6]
    })
    result_df, _ = task_func(df)
    assert result_df.equals(expected_df)

def test_task_func_plot():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    _, ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Boxplot of Last Column'
    assert ax.get_xlabel() == 'B'

def test_task_func_no_missing_values():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    result_df, _ = task_func(df)
    assert result_df.equals(df)