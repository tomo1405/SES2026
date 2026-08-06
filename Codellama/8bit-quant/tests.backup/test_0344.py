import pytest
from src_0344 import task_func
import pandas as pd

def test_task_func_empty_df():
    df = pd.DataFrame()
    col = 'a'
    with pytest.raises(ValueError):
        task_func(df, col)

def test_task_func_invalid_col():
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    col = 'c'
    with pytest.raises(ValueError):
        task_func(df, col)

def test_task_func_valid_input():
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    col = 'a'
    ax = task_func(df, col)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Value Counts'
    assert len(ax.get_legend().get_texts()) == 2
    assert ax.get_legend().get_texts()[0].get_text() == 'a'
    assert ax.get_legend().get_texts()[1].get_text() == 'b'

def test_task_func_valid_input_with_title():
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    col = 'a'
    title = 'My Pie Chart'
    ax = task_func(df, col, title)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == title
    assert len(ax.get_legend().get_texts()) == 2
    assert ax.get_legend().get_texts()[0].get_text() == 'a'
    assert ax.get_legend().get_texts()[1].get_text() == 'b'