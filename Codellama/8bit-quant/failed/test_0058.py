import pytest
from src_0058 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def test_task_func():
    csv_file_path = 'test_data.csv'
    title = 'Test Heatmap'
    corr, ax = task_func(csv_file_path, title)
    assert isinstance(corr, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert corr.shape == (10, 10)
    assert ax.get_title() == title
    assert ax.get_xlabel() == 'X'
    assert ax.get_ylabel() == 'Y'
    assert ax.get_xlim() == (0, 10)
    assert ax.get_ylim() == (0, 10)
    assert ax.get_xticks() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert ax.get_yticks() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert ax.get_xticklabels() == ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10']
    assert ax.get_yticklabels() == ['Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Y10']
    assert ax.get_cmap() == 'coolwarm'
    assert ax.get_cbar() == True