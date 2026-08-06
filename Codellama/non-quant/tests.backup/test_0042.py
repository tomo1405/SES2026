import pytest
from src_0042 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew

def test_task_func():
    data_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    df, ax = task_func(data_matrix)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (3, 1)
    assert ax.get_title() == "Distribution of Skewness"
    assert ax.get_xlabel() == "Skewness"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_xlim() == (0, 10)
    assert ax.get_ylim() == (0, 10)
    assert ax.get_xticks() == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert ax.get_yticks() == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert ax.get_xticklabels() == ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    assert ax.get_yticklabels() == ["1", "2", "3", "4", "5", "6", "7", "8", "9"]