import pytest
from src_0134 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_input_validation():
    with pytest.raises(ValueError):
        task_func(None)
    with pytest.raises(ValueError):
        task_func(pd.DataFrame())

def test_task_func_normalization():
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(data)
    normalized_df, ax = task_func(df)
    
    assert isinstance(normalized_df, pd.DataFrame)
    assert normalized_df.equals(df)
    assert 'B' in normalized_df.columns
    
    # Check if the last column is normalized
    expected_normalized_values = MinMaxScaler().fit_transform(df[['B']]).flatten()
    assert np.allclose(normalized_df['B'], expected_normalized_values)

def test_task_func_plot():
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(data)
    normalized_df, ax = task_func(df)
    
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Normalized Data of B'
    assert ax.get_xlabel() == 'Index'
    assert ax.get_ylabel() == 'Normalized Value'