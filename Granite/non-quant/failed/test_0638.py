import pytest
from src_0638 import task_func

def test_task_func():
    num_students = 10
    df, ax = task_func(num_students)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (num_students, 5)
    assert ax.get_title() == 'Course-wise Average and Passing Grade Counts'