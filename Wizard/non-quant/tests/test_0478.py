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
    assert len(df["category"].unique()) == 5
    assert len(ax.get_legend_handles_labels()[0]) == 5