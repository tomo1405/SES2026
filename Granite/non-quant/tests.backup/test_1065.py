import numpy as np
import seaborn as sns
import pytest

def task_func(arr):
    row_sums = arr.sum(axis=1)
    vmax = np.max(arr)  # Set vmax to the maximum value in the array
    vmin = np.min(arr)  # Set vmin to the minimum value in the array
    ax = sns.heatmap(
        arr, annot=True, vmax=vmax, vmin=vmin
    )  # Include both vmin and vmax in the heatmap call
    ax.set_title("Heatmap of the 2D Array")

    return ax

def test_task_func():
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    ax = task_func(arr)
    assert ax.get_title() == "Heatmap of the 2D Array"
    assert ax.get_children()[0].get_text() == "1"
    assert ax.get_children()[1].get_text() == "2"
    assert ax.get_children()[2].get_text() == "3"
    assert ax.get_children()[3].get_text() == "4"
    assert ax.get_children()[4].get_text() == "5"
    assert ax.get_children()[5].get_text() == "6"
    assert ax.get_children()[6].get_text() == "7"
    assert ax.get_children()[7].get_text() == "8"
    assert ax.get_children()[8].get_text() == "9"