import pytest
from src_0140 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_valid_input():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    axes = task_func(df)
    assert isinstance(axes, list)
    assert len(axes) == 2
    assert all(isinstance(ax, plt.Axes) for ax in axes)

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(None)
    with pytest.raises(ValueError):
        task_func(pd.DataFrame())
    with pytest.raises(ValueError):
        task_func(pd.DataFrame({'A': ['a', 'b', 'c']}))