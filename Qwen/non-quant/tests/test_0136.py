import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest
from src_0136 import task_func


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
    df_imputed, ax = task_func(df)
    assert df_imputed['B'].isnull().sum() == 0
    assert df_imputed['B'].mean() == pytest.approx(5.0)

def test_task_func_boxplot():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    df_imputed, ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Boxplot of Last Column'
    assert ax.get_xlabel() == 'B'

def test_task_func_no_missing_values():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    df_imputed, ax = task_func(df)
    assert df_imputed.equals(df)

def test_task_func_single_column():
    df = pd.DataFrame({
        'A': [1, 2, np.nan]
    })
    df_imputed, ax = task_func(df)
    assert df_imputed['A'].isnull().sum() == 0
    assert df_imputed['A'].mean() == pytest.approx(2.0)