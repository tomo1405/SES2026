python
import pandas as pd
import matplotlib.pyplot as plt
import pytest

def task_func(array):
    # Internal Constants
    COLUMNS = ["A", "B", "C", "D", "E"]

    df = pd.DataFrame(array, columns=COLUMNS)
    sums = df.sum()

    fig, ax = plt.subplots()
    sums.plot(kind="bar", ax=ax)

    return df, ax

def test_task_func():
    # Test Case 1
    array = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
    expected_df = pd.DataFrame([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], columns=["A", "B", "C", "D", "E"])
    expected_ax = None

    df, ax = task_func(array)

    assert df.equals(expected_df)
    assert ax == expected_ax

    # Test Case 2
    array = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
    expected_df = pd.DataFrame([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], columns=["A", "B", "C", "D", "E"])
    expected_ax = None

    df, ax = task_func(array)

    assert df.equals(expected_df)
    assert ax == expected_ax

    # Test Case 3
    array = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
    expected_df = pd.DataFrame([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], columns=["A", "B", "C", "D", "E"])
    expected_ax = None

    df, ax = task_func(array)

    assert df.equals(expected_df)
    assert ax == expected_ax