import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from src_0637 import task_func


def test_task_func_with_rows_less_than_or_equal_to_zero():
    df, ax = task_func(0)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.empty
    assert ax.get_title() == 'Non-Zero Value Counts'

def test_task_func_with_rows_greater_than_zero():
    rows = 10
    df, ax = task_func(rows)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert not df.empty
    assert ax.get_title() == 'Non-Zero Value Counts'
    assert df.shape == (rows, len(COLUMNS))
    assert (df.astype(bool).sum(axis=0) == np.array([10, 10, 10, 10, 10])).all()