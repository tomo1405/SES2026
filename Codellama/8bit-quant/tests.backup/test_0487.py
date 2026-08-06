import pytest
from src_0487 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    start_time = 1640995200000
    end_time = 1640995200000 + 1000
    step = 100
    trend = 1
    seed = 42

    ax = task_func(start_time, end_time, step, trend, seed)

    assert isinstance(ax, pd.plotting.matplotlib.axes.Axes)
    assert ax.get_xlabel() == "Time"
    assert ax.get_ylabel() == "Value"
    assert len(ax.get_lines()) == 1
    assert ax.get_lines()[0].get_label() == "Value"
    assert ax.get_lines()[0].get_xdata().shape == (10,)
    assert ax.get_lines()[0].get_ydata().shape == (10,)