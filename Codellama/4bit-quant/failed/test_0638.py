import pytest
from src_0638 import task_func

def test_task_func():
    # Test with num_students = 10
    df, ax = task_func(10)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert len(df) == 10
    assert len(df.columns) == 5
    assert len(df.index) == 10
    assert df.mean().shape == (5,)
    assert df[df >= 60].count().shape == (5,)
    assert ax.get_title() == 'Course-wise Average and Passing Grade Counts'
    assert ax.get_legend() is not None

    # Test with num_students = 20
    df, ax = task_func(20)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert len(df) == 20
    assert len(df.columns) == 5
    assert len(df.index) == 20
    assert df.mean().shape == (5,)
    assert df[df >= 60].count().shape == (5,)
    assert ax.get_title() == 'Course-wise Average and Passing Grade Counts'
    assert ax.get_legend() is not None

    # Test with num_students = 30
    df, ax = task_func(30)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert len(df) == 30
    assert len(df.columns) == 5
    assert len(df.index) == 30
    assert df.mean().shape == (5,)
    assert df[df >= 60].count().shape == (5,)
    assert ax.get_title() == 'Course-wise Average and Passing Grade Counts'
    assert ax.get_legend() is not None