python
import pytest
from src_0985 import task_func

def test_task_func():
    df = {"x": [1, 2, 3], "y": [2, 4, 6]}
    x_column = "x"
    y_column = "y"
    ax = task_func(df, x_column, y_column)
    assert isinstance(ax, plt.Axes)