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
    assert ax.get_xticks() == range(11)
    assert ax.get_yticks() == range(11)
    assert ax.get_xticklabels() == [f'X{i}' for i in range(11)]
    assert ax.get_yticklabels() == [f'Y{i}' for i in range(11)]
    assert ax.get_cmap() == 'coolwarm'
    assert ax.get_cbar() == True