import pytest
from src_1026 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler


def test_task_func_empty_data():
    data_dict = {}
    df, ax = task_func(data_dict)
    assert df.empty
    assert ax.get_title() == PLOT_TITLE


def test_task_func_non_empty_data():
    data_dict = {"a": [1, 2, 3], "b": [4, 5, 6]}
    df, ax = task_func(data_dict)
    assert not df.empty
    assert ax.get_title() == PLOT_TITLE
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.columns.tolist() == ["a", "b"]
    assert df.shape == (3, 2)
    assert ax.get_xlabel() == "a"
    assert ax.get_ylabel() == "b"