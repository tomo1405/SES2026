import pytest
from src_0113 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_valid_input():
    df = pd.DataFrame({'Status': ['A', 'B', 'C']})
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Status Distribution'
    assert ax.get_legend() == 'Status'
    assert ax.get_ylabel() == 'Count'
    assert ax.get_xlabel() == 'Status'

def test_task_func_invalid_input():
    df = pd.DataFrame({'Status': ['A', 'B', 'C']})
    with pytest.raises(ValueError):
        task_func(df)