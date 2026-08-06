import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from src_0043 import task_func


def test_task_func():
    data_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    df, ax = task_func(data_matrix)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (3, 3)
    assert df.columns[0] == "Component 1"
    assert df.columns[-1] == "Mean"
    assert df["Mean"].mean() == df.mean().mean()
    assert ax.get_xlabel() == "Number of Components"
    assert ax.get_ylabel() == "Cumulative Explained Variance"

def test_task_func_n_components():
    data_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    df, ax = task_func(data_matrix, n_components=1)
    assert df.shape == (3, 2)
    assert df.columns[0] == "Component 1"
    assert df.columns[-1] == "Mean"
    assert ax.get_xlabel() == "Number of Components"
    assert ax.get_ylabel() == "Cumulative Explained Variance"