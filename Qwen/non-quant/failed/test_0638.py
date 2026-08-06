import pytest
from src_0638 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def test_task_func_output():
    num_students = 10
    df, ax = task_func(num_students)

    # Check DataFrame shape
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (num_students, 5)

    # Check DataFrame index
    assert all(isinstance(idx, str) for idx in df.index)
    assert len(set(df.index)) == num_students

    # Check DataFrame columns
    expected_columns = ['Course1', 'Course2', 'Course3', 'Course4', 'Course5']
    assert list(df.columns) == expected_columns

    # Check grades range
    assert df.values.min() >= 40
    assert df.values.max() <= 100

    # Check plot type
    assert isinstance(ax, plt.Axes)

def test_task_func_edge_cases():
    # Test with minimum number of students
    df_min, ax_min = task_func(1)
    assert df_min.shape == (1, 5)

    # Test with maximum number of students
    df_max, ax_max = task_func(100)
    assert df_max.shape == (100, 5)

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(0)  # Invalid number of students

    with pytest.raises(ValueError):
        task_func(-10)  # Negative number of students

    with pytest.raises(ValueError):
        task_func(101)  # More students than available