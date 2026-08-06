import matplotlib.pyplot as plt
import pandas as pd
from src_0637 import task_func


def test_task_func_zero_rows():
    df, ax = task_func(0)
    assert isinstance(df, pd.DataFrame)
    assert df.empty
    assert df.columns.tolist() == COLUMNS
    assert ax.get_title() == 'Non-Zero Value Counts'
    assert plt.fignum_exists(1) is False

def test_task_func_negative_rows():
    df, ax = task_func(-5)
    assert isinstance(df, pd.DataFrame)
    assert df.empty
    assert df.columns.tolist() == COLUMNS
    assert ax.get_title() == 'Non-Zero Value Counts'
    assert plt.fignum_exists(1) is False

def test_task_func_positive_rows():
    df, ax = task_func(5)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, len(COLUMNS))
    assert df.columns.tolist() == COLUMNS
    assert ax.get_title() == 'Non-Zero Value Counts'
    assert plt.fignum_exists(1) is True
    plt.close('all')

def test_task_func_non_empty_counts():
    df, ax = task_func(5)
    counts = df.astype(bool).sum(axis=0)
    bar_heights = [rect.get_height() for rect in ax.patches]
    assert counts.tolist() == bar_heights
    plt.close('all')