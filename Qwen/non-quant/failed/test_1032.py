import pytest
from src_1032 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(n_rows=-1)
    with pytest.raises(ValueError):
        task_func(n_rows=0)

def test_task_func_output_type():
    ax = task_func(n_rows=10)
    assert isinstance(ax, plt.Axes)

def test_task_func_dataframe_content():
    df = task_func(n_rows=10)
    assert isinstance(df, pd.DataFrame)
    assert "String" in df.columns
    assert len(df) == 10

def test_task_func_string_length():
    df = task_func(n_rows=10)
    for s in df["String"]:
        assert len(s) == 3

def test_task_func_plot_title():
    ax = task_func(n_rows=10)
    assert ax.get_title() == "Top 30 Frequencies of Random 3-Letter Strings"

def test_task_func_plot_labels():
    ax = task_func(n_rows=10)
    assert ax.get_xlabel() == "String"
    assert ax.get_ylabel() == "Frequency"