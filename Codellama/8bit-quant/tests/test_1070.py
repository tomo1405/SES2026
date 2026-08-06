import pytest
from src_1070 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    data_dict = {"a": [1, 2, 3, 4, 5], "b": [1, 2, 3, 4, 5], "c": [1, 2, 3, 4, 5]}
    df = pd.DataFrame(data_dict)
    axes_list = task_func(data_dict)
    assert len(axes_list) == 3
    for ax in axes_list:
        assert isinstance(ax, plt.Axes)
        assert ax.get_title() in df.columns
        assert len(ax.get_xticks()) == len(df[ax.get_title()].value_counts())
        assert len(ax.get_yticks()) == len(df[ax.get_title()].value_counts())

def test_task_func_uniform_distribution():
    data_dict = {"a": [1, 1, 1, 1, 1], "b": [1, 1, 1, 1, 1], "c": [1, 1, 1, 1, 1]}
    df = pd.DataFrame(data_dict)
    axes_list = task_func(data_dict)
    assert len(axes_list) == 3
    for ax in axes_list:
        assert isinstance(ax, plt.Axes)
        assert ax.get_title() in df.columns
        assert len(ax.get_xticks()) == len(df[ax.get_title()].value_counts())
        assert len(ax.get_yticks()) == len(df[ax.get_title()].value_counts())

def test_task_func_non_uniform_distribution():
    data_dict = {"a": [1, 2, 3, 4, 5], "b": [1, 2, 3, 4, 5], "c": [1, 2, 3, 4, 5]}
    df = pd.DataFrame(data_dict)
    axes_list = task_func(data_dict)
    assert len(axes_list) == 3
    for ax in axes_list:
        assert isinstance(ax, plt.Axes)
        assert ax.get_title() in df.columns
        assert len(ax.get_xticks()) == len(df[ax.get_title()].value_counts())
        assert len(ax.get_yticks()) == len(df[ax.get_title()].value_counts())