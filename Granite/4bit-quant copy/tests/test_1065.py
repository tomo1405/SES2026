import pytest
from src_1065 import task_func
import numpy as np
import seaborn as sns

def test_task_func():
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    ax = task_func(arr)
    assert ax.get_title() == "Heatmap of the 2D Array"
    assert ax.get_xlabel() == "x-axis"
    assert ax.get_ylabel() == "y-axis"
    assert ax.get_zlabel() == "value"