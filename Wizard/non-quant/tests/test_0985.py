python
import pytest
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from src_0985 import task_func

def test_task_func():
    df = {"x": [1, 2, 3, 4, 5], "y": [2, 4, 6, 8, 10]}
    x_column = "x"
    y_column = "y"
    ax = task_func(df, x_column, y_column)
    assert isinstance(ax, plt.Axes)