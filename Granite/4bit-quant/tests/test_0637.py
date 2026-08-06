import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from src_0637 import task_func

# Constants
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

def test_task_func_with_rows_less_than_or_equal_to_zero():
    df, ax = task_func(0)
    assert isinstance(df, pd.DataFrame)
    assert df.columns.tolist() == COLUMNS
    assert len(df) == 0
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Non-Zero Value Counts'

def test_task_func_with_rows_greater_than_zero():
    rows = 10
    df, ax = task_func(rows)
    assert isinstance(df, pd.DataFrame)
    assert df.columns.tolist() == COLUMNS
    assert len(df) == rows
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Non-Zero Value Counts'
    assert (df > 0).sum().all()