import pandas as pd
import matplotlib.pyplot as plt
from src_0344 import task_func

# Constants for pie chart colors
COLORS = ['r', 'g', 'b', 'y', 'm']

def test_task_func_valid_input():
    df = pd.DataFrame({'col': ['a', 'b', 'a', 'c', 'b']})
    ax = task_func(df, 'col')
    assert isinstance(ax, plt.Axes)

def test_task_func_invalid_input():
    df = pd.DataFrame({'col': ['a', 'b', 'a', 'c', 'b']})
    with pytest.raises(ValueError):
        task_func(df, 'non_existent_col')

def test_task_func_title():
    df = pd.DataFrame({'col': ['a', 'b', 'a', 'c', 'b']})
    title = 'My Pie Chart'
    ax = task_func(df, 'col', title=title)
    assert ax.get_title() == title