import pytest
from src_0637 import task_func

def test_task_func():
    # Test with valid input
    rows = 10
    df, ax = task_func(rows)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (rows, len(COLUMNS))
    assert ax.get_title() == 'Non-Zero Value Counts'

    # Test with invalid input
    rows = 0
    df, ax = task_func(rows)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (0, len(COLUMNS))
    assert ax.get_title() == 'Non-Zero Value Counts'

    # Test with valid input
    rows = 100
    df, ax = task_func(rows)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (rows, len(COLUMNS))
    assert ax.get_title() == 'Non-Zero Value Counts'

    # Test with invalid input
    rows = -10
    df, ax = task_func(rows)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (0, len(COLUMNS))
    assert ax.get_title() == 'Non-Zero Value Counts'