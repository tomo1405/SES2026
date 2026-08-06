python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

from src_0478 import task_func

def test_task_func():
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert len(df) == 100
    assert len(set(df["category"])) == 5
    assert all(isinstance(x, float) for x in df["x"])
    assert all(isinstance(x, float) for x in df["y"])
    assert all(isinstance(x, str) for x in df["category"])
    assert all(isinstance(x, str) for x in ax.get_legend_handles_labels()[1])