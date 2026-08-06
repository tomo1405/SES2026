import matplotlib
import pandas as pd
from src_1034 import task_func


def test_task_func():
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert len(df) == 26
    assert len(df.columns) == 3
    assert all(df.columns == ["a", "b", "c"])
    assert all(df["a"].value_counts().index == LETTERS)
    assert all(df["a"].value_counts().values == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    assert all(ax.get_xticklabels() == LETTERS)
    assert all(ax.get_yticklabels() == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])