import pytest
from src_1032 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_invalid_n_rows():
    with pytest.raises(ValueError):
        task_func(n_rows=-1)
    with pytest.raises(ValueError):
        task_func(n_rows=0)

def test_task_func_return_type():
    ax = task_func(n_rows=10)
    assert isinstance(ax, plt.Axes)

def test_task_func_data_generation():
    df = task_func(n_rows=10)
    data = df.get_figure().get_axes()[0].patches
    assert len(data) == 30  # Only top 30 frequencies are plotted

def test_task_func_dataframe_content():
    df = task_func(n_rows=10)
    data = df.get_figure().get_axes()[0].get_xticklabels()
    for label in data:
        assert len(label.get_text()) == 3  # Each string should be 3 characters long

def test_task_func_plot_title():
    df = task_func(n_rows=10)
    title = df.get_figure().get_axes()[0].get_title()
    assert title == "Top 30 Frequencies of Random 3-Letter Strings"

def test_task_func_plot_labels():
    df = task_func(n_rows=10)
    xlabel = df.get_figure().get_axes()[0].get_xlabel()
    ylabel = df.get_figure().get_axes()[0].get_ylabel()
    assert xlabel == "String"
    assert ylabel == "Frequency"