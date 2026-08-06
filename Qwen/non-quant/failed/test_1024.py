import pytest
from src_1024 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func_empty_dataframe():
    df = pd.DataFrame()
    with pytest.raises(ValueError, match="DataFrame is empty."):
        task_func(df)

def test_task_func_non_numeric_columns():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': ['a', 'b', 'c']
    })
    with pytest.raises(TypeError, match="All columns must be numeric for correlation calculation."):
        task_func(df)

def test_task_func_single_column():
    df = pd.DataFrame({
        'A': [1, 2, 3]
    })
    with pytest.raises(ValueError, match="DataFrame must have at least two columns for correlation calculation."):
        task_func(df)

def test_task_func_valid_input():
    df = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [4, 3, 2, 1],
        'C': [2, 3, 4, 5]
    })
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    # Capture the plot as an image and compare it (this part is more complex and may require additional setup)

def test_task_func_identical_columns():
    df = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [1, 2, 3, 4]
    })
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    # Capture the plot as an image and compare it (this part is more complex and may require additional setup)

# Additional helper functions to capture and compare plots can be added here if needed