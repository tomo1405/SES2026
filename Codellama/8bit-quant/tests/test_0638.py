import matplotlib.pyplot as plt
import pandas as pd
from src_0638 import task_func


def test_task_func():
    num_students = 10
    df, ax = task_func(num_students)

    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert len(df) == num_students
    assert len(df.columns) == len(COURSES)
    assert len(df.index) == len(STUDENTS)
    assert all(df.index == students_sample)
    assert all(df.columns == COURSES)
    assert all(df >= 0)
    assert all(df <= 100)
    assert all(df.mean() >= 0)
    assert all(df.mean() <= 100)
    assert all(df[df >= 60].count() >= 0)
    assert all(df[df >= 60].count() <= num_students)
    assert ax.get_title() == 'Course-wise Average and Passing Grade Counts'
    assert ax.get_legend() is not None