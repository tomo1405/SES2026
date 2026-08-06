import re
import matplotlib.pyplot as plt
import pandas as pd
import pytest

from src_0176 import task_func

@pytest.fixture
def df():
    return pd.DataFrame({
        'Likes': [100, 200, 300, 400],
        'Views': [50, 100, 150, 200],
        'Title': ['How to Train Your Dragon', 'Harry Potter', 'The Lion King', 'The Little Prince']
    })

def test_task_func_with_valid_df(df):
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_empty_df(df):
    df = pd.DataFrame()
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_missing_columns(df):
    df = df.drop(columns=['Likes', 'Views'])
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_no_interesting_videos(df):
    df = df.drop(index=[0, 1])
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_interesting_videos(df):
    df = df.copy()  # Create a copy to avoid modifying the input df
    df.loc[0, 'Likes'] = 1000
    df.loc[0, 'Views'] = 100
    df.loc[0, 'Title'] = 'How to Train Your Dragon 2'
    df.loc[1, 'Likes'] = 2000
    df.loc[1, 'Views'] = 200
    df.loc[1, 'Title'] = 'Harry Potter 2'
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)