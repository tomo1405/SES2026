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
    assert all(df.index == ['Student' + str(i) for i in range(1, 11)])
    assert all(df.columns == ['Course' + str(i) for i in range(1, 6)])
    assert all(df.mean() >= 40)
    assert all(df.mean() <= 100)
    assert all(df[df >= 60].count() >= 0)
    assert all(df[df >= 60].count() <= 10)
    assert ax.get_title() == 'Course-wise Average and Passing Grade Counts'
    assert ax.get_legend() == ['Average Grade', 'Passing Grade Counts']

    # Test with num_students = 50
    df, ax = task_func(50)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert len(df) == 50
    assert len(df.columns) == 5
    assert len(df.index) == 50
    assert all(df.index == ['Student' + str(i) for i in range(1, 51)])
    assert all(df.columns == ['Course' + str(i) for i in range(1, 6)])
    assert all(df.mean() >= 40)
    assert all(df.mean() <= 100)
    assert all(df[df >= 60].count() >= 0)
    assert all(df[df >= 60].count() <= 50)
    assert ax.get_title() == 'Course-wise Average and Passing Grade Counts'
    assert ax.get_legend() == ['Average Grade', 'Passing Grade Counts']

    # Test with num_students = 100
    df, ax = task_func(100)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert len(df) == 100
    assert len(df.columns) == 5
    assert len(df.index) == 100
    assert all(df.index == ['Student' + str(i) for i in range(1, 101)])
    assert all(df.columns == ['Course' + str(i) for i in range(1, 6)])
    assert all(df.mean() >= 40)
    assert all(df.mean() <= 100)
    assert all(df[df >= 60].count() >= 0)
    assert all(df[df >= 60].count() <= 100)
    assert ax.get_title() == 'Course-wise Average and Passing Grade Counts'
    assert ax.get_legend() == ['Average Grade', 'Passing Grade Counts']