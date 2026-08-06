import pytest
from src_1026 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

def test_task_func():
    data_dict = {'a': [1, 2, 3], 'b': [4, 5, 6]}
    df, ax = task_func(data_dict)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (3, 2)
    assert ax.get_title() == "Scaled Values"

def test_task_func_empty_data():
    data_dict = {'a': [], 'b': []}
    df, ax = task_func(data_dict)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.empty
    assert ax.get_title() == "Scaled Values"

def test_task_func_invalid_data():
    data_dict = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
    with pytest.raises(ValueError):
        task_func(data_dict)