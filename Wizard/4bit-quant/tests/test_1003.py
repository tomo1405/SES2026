python
import pandas as pd
import matplotlib.pyplot as plt
import pytest

from src_1003 import task_func

def test_task_func():
    data = {"col1": [1, 2, 3], "col2": [4, 5, 6]}
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Histogram of target_column"
    assert ax.get_xlabel() == "target_column"
    assert ax.get_ylabel() == "Frequency"
    assert len(ax.patches) == 3
    assert ax.patches[0].get_height() == 1
    assert ax.patches[1].get_height() == 1
    assert ax.patches[2].get_height() == 1