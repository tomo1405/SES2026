import pytest
from src_0342 import task_func
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def test_task_func_valid_input():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})
    col = 'A'
    fig = task_func(df, col)
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 2
    assert fig.axes[0].get_title() == 'Histogram of A'
    assert fig.axes[1].get_title() == 'Boxplot of A'

def test_task_func_invalid_input():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})
    col = 'C'
    with pytest.raises(ValueError):
        task_func(df, col)