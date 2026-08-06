import matplotlib.pyplot as plt
import pandas as pd
from src_0478 import task_func


def test_task_func():
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert len(df) == 100
    assert len(df["category"].unique()) <= len(task_func.CATEGORIES)
    for category in task_func.CATEGORIES:
        assert category in df["category"].unique()
    assert ax.get_legend_handles_labels()[1] == task_func.CATEGORIES