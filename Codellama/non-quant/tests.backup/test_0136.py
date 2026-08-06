import pytest
from src_0136 import task_func
import numpy as np
import pandas as pd

def test_task_func_input_type():
    with pytest.raises(ValueError):
        task_func(1)

def test_task_func_input_empty_df():
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_input_non_empty_df():
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    df, ax = task_func(df)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert df.shape == (3, 2)
    assert ax.get_title() == 'Boxplot of Last Column'
    assert ax.get_xlabel() == 'b'