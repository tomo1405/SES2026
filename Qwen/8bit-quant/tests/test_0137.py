import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest
from src_0137 import task_func


def test_task_func_input_type():
    with pytest.raises(ValueError, match="Input must be a DataFrame"):
        task_func([1, 2, 3])

def test_task_func_empty_dataframe():
    df = pd.DataFrame()
    with pytest.raises(ValueError, match="DataFrame is empty"):
        task_func(df)

def test_task_func_valid_input():
    data = {
        'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8]
    }
    df = pd.DataFrame(data)
    pca_df, ax = task_func(df)
    
    assert isinstance(pca_df, pd.DataFrame)
    assert pca_df.shape == (4, 2)
    assert list(pca_df.columns) == ['Principal Component 1', 'Principal Component 2']
    
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == '2 Component PCA'
    assert ax.get_xlabel() == 'Principal Component 1'
    assert ax.get_ylabel() == 'Principal Component 2'

def test_task_func_with_random_data():
    np.random.seed(0)
    data = np.random.rand(10, 5)
    df = pd.DataFrame(data)
    pca_df, ax = task_func(df)
    
    assert isinstance(pca_df, pd.DataFrame)
    assert pca_df.shape == (10, 2)
    assert list(pca_df.columns) == ['Principal Component 1', 'Principal Component 2']
    
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == '2 Component PCA'
    assert ax.get_xlabel() == 'Principal Component 1'
    assert ax.get_ylabel() == 'Principal Component 2'