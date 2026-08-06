import pytest
from src_0606 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ax = task_func(matrix)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_invalid_input():
    with pytest.raises(ValueError):
        task_func("not a list of lists")