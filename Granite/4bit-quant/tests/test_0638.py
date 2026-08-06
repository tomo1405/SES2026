import matplotlib.pyplot as plt
import pandas as pd
import pytest
from src_0638 import task_func


def test_task_func():
    # Test case 1: num_students = 5
    num_students = 5
    df, ax = task_func(num_students)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (num_students, 5)
    assert ax.get_title() == 'Course-wise Average and Passing Grade Counts'
    assert list(df.index) == ['Student' + str(i) for i in range(1, 6)]
    assert list(df.columns) == ['Course' + str(i) for i in range(1, 6)]

    # Test case 2: num_students = 10
    num_students = 10
    df, ax = task_func(num_students)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (num_students, 5)
    assert ax.get_title() == 'Course-wise Average and Passing Grade Counts'
    assert list(df.index) == ['Student' + str(i) for i in range(1, 11)]
    assert list(df.columns) == ['Course' + str(i) for i in range(1, 6)]

if __name__ == "__main__":
    pytest.main()