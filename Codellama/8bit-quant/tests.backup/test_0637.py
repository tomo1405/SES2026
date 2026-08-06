import pytest
from src_0637 import task_func

def test_task_func_positive_rows():
    rows = 10
    df, ax = task_func(rows)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (rows, len(COLUMNS))
    assert ax.get_title() == 'Non-Zero Value Counts'

def test_task_func_negative_rows():
    rows = -1
    df, ax = task_func(rows)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (0, len(COLUMNS))
    assert ax.get_title() == 'Non-Zero Value Counts'

def test_task_func_zero_rows():
    rows = 0
    df, ax = task_func(rows)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (0, len(COLUMNS))
    assert ax.get_title() == 'Non-Zero Value Counts'