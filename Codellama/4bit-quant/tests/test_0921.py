import pytest
from src_0921 import task_func
import pandas as pd
import seaborn as sns

def test_task_func():
    data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
    ax = task_func(data)
    assert isinstance(ax, sns.heatmap)
    assert ax.title.get_text() == 'Correlation Matrix'
    assert ax.get_xlabel() == 'A'
    assert ax.get_ylabel() == 'B'
    assert ax.get_zlabel() == 'C'
    assert ax.get_zlim() == (0, 1)
    assert ax.get_cmap() == 'coolwarm'
    assert ax.get_annot() == True