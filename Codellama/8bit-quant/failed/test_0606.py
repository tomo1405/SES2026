import pytest
from src_0606 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ax = task_func(matrix)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'X'
    assert ax.get_ylabel() == 'Y'
    assert ax.get_title() == 'Heatmap'
    assert ax.get_cmap() == 'hot'
    assert ax.get_interpolation() == 'nearest'
    assert ax.get_data() == matrix