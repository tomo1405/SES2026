import pytest
from src_1065 import task_func
import numpy as np
import seaborn as sns

def test_task_func():
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    ax = task_func(arr)
    assert isinstance(ax, sns.heatmap)
    assert ax.get_title() == "Heatmap of the 2D Array"
    assert np.array_equal(ax.get_array(), arr)
    assert ax.get_vmax() == np.max(arr)
    assert ax.get_vmin() == np.min(arr)
    assert ax.get_annot() == True