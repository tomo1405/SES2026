import pytest
from src_0140 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_input_type():
    with pytest.raises(ValueError):
        task_func(1)

def test_task_func_input_empty_df():
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_numeric_cols():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    numeric_cols = df.select_dtypes(include=np.number).columns
    assert numeric_cols.size == 2

def test_task_func_axes():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    axes = task_func(df)
    assert len(axes) == 2
    for ax in axes:
        assert isinstance(ax, plt.Axes)