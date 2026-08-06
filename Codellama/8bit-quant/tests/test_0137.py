import pytest
from src_0137 import task_func
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def test_task_func_input_not_dataframe():
    with pytest.raises(ValueError):
        task_func(1)

def test_task_func_input_empty_dataframe():
    with pytest.raises(ValueError):
        task_func(pd.DataFrame())

def test_task_func_output_dataframe():
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    pca_df, ax = task_func(df)
    assert isinstance(pca_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)

def test_task_func_output_axes():
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    pca_df, ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'Principal Component 1'
    assert ax.get_ylabel() == 'Principal Component 2'
    assert ax.get_title() == '2 Component PCA'