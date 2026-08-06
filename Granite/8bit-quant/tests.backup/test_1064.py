import pytest
from src_1064 import task_func

def test_task_func():
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Replace this with your own input data
    ax = task_func(arr)
    assert ax is not None  # Check if the returned ax object is not None
    assert ax.get_title() == "Explained Variance Ratio of Principal Components"  # Check if the title is correct
    assert ax.get_xticks()[0] == 0  # Check if the x-tick is correct
    assert ax.get_xticklabels()[0] == "PC1"  # Check if the x-tick label is correct