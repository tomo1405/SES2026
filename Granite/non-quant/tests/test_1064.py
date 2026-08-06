import pytest
from src_1064 import task_func

def test_task_func():
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ax = task_func(arr)
    assert ax is not None
    assert ax.get_title() == "Explained Variance Ratio of Principal Components"
    assert ax.get_xticks() == [0]
    assert ax.get_xticklabels() == ["PC1"]