import pandas as pd
from matplotlib import pyplot as plt
import pytest

def task_func(arr):
    if not arr.size:  # Check for empty array
        _, ax = plt.subplots()
        ax.set_title("Time Series of Row Sums")
        return ax

    row_sums = arr.sum(axis=1)
    df = pd.DataFrame(row_sums, columns=["Sum"])
    df.index = pd.date_range(start="1/1/2020", periods=df.shape[0])
    ax = df.plot(title="Time Series of Row Sums")
    return ax

def test_task_func():
    # Test case 1: Empty array
    arr = pd.DataFrame([])
    expected_ax_title = "Time Series of Row Sums"
    ax = task_func(arr)
    assert ax.get_title() == expected_ax_title

    # Test case 2: Non-empty array
    arr = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    expected_ax_title = "Time Series of Row Sums"
    ax = task_func(arr)
    assert ax.get_title() == expected_ax_title