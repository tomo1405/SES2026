import pytest
from src_0136 import task_func
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt

def test_task_func_input_not_dataframe():
    with pytest.raises(ValueError):
        task_func(1)

def test_task_func_input_empty_dataframe():
    with pytest.raises(ValueError):
        task_func(pd.DataFrame())

def test_task_func_input_valid_dataframe():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df, ax = task_func(df)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (3, 2)
    assert ax.get_title() == 'Boxplot of Last Column'
    assert ax.get_xlabel() == 'B'

def test_task_func_impute_mean():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, np.nan, 6]})
    df, ax = task_func(df)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (3, 2)
    assert ax.get_title() == 'Boxplot of Last Column'
    assert ax.get_xlabel() == 'B'
    assert np.allclose(df['B'], [4, 5, 6])