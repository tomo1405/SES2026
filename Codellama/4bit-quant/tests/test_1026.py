import matplotlib.pyplot as plt
import pandas as pd
from src_1026 import task_func


def test_task_func():
    data_dict = {'a': [1, 2, 3], 'b': [4, 5, 6]}
    df, ax = task_func(data_dict)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.equals(pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]}))
    assert ax.get_title() == 'Scaled Values'

def test_task_func_empty_data():
    data_dict = {'a': [], 'b': []}
    df, ax = task_func(data_dict)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.empty
    assert ax.get_title() == 'Scaled Values'

def test_task_func_invalid_data():
    data_dict = {'a': [1, 2, 3], 'b': [4, 5, 6]}
    df, ax = task_func(data_dict)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.equals(pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]}))
    assert ax.get_title() == 'Scaled Values'