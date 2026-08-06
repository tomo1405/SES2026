import pytest
from src_1066 import task_func

def test_task_func():
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Replace this with your own input data
    ax = task_func(arr)
    assert ax is not None  # Check if the function returns a valid output
    assert ax.plot is not None  # Check if the output has a valid plot attribute
    assert ax.set_title is not None  # Check if the output has a valid set_title attribute