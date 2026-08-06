import matplotlib.pyplot as plt
import pandas as pd
import pytest
from src_0344 import task_func

# Constants for pie chart colors
COLORS = ['r', 'g', 'b', 'y', 'm']

def test_task_func_valid_input():
    df = pd.DataFrame({'col': [1, 2, 3, 4, 5]})
    ax = task_func(df, 'col')
    assert isinstance(ax, plt.Axes)

def test_task_func_invalid_input():
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df, 'col')

def test_task_func_title():
    df = pd.DataFrame({'col': [1, 2, 3, 4, 5]})
    ax = task_func(df, 'col', title='My Pie Chart')
    assert ax.get_title() == 'My Pie Chart'