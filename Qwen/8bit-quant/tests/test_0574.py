import pytest
from src_0574 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_output():
    df, ax = task_func(10)
    
    # Check if the DataFrame has the correct shape
    assert df.shape == (3, 2), "DataFrame should have 3 rows and 2 columns"
    
    # Check if the DataFrame contains the correct index
    expected_index = ['Mean', 'Median', 'Standard Deviation']
    assert list(df.index) == expected_index, "DataFrame index should match the expected values"
    
    # Check if the DataFrame contains the correct columns
    expected_columns = ['Array1', 'Array2']
    assert list(df.columns) == expected_columns, "DataFrame columns should match the expected values"
    
    # Check if the DataFrame contains numerical data
    assert np.issubdtype(df.dtypes[0], np.number), "DataFrame values should be numerical"
    
    # Check if the plot is of type AxesSubplot
    assert isinstance(ax, plt.Axes), "The returned plot should be an instance of matplotlib.axes._subplots.AxesSubplot"

def test_task_func_default_length():
    df, _ = task_func()
    assert df.shape == (3, 2), "Default array length should be 100, resulting in a DataFrame with 3 rows and 2 columns"

def test_task_func_custom_length():
    df, _ = task_func(50)
    assert df.shape == (3, 2), "Custom array length should result in a DataFrame with 3 rows and 2 columns"