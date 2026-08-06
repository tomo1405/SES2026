import pandas as pd
from src_0176 import task_func


def test_task_func_empty_df():
    df = pd.DataFrame()
    ax = task_func(df)
    assert ax.get_figure().get_axes() == []

def test_task_func_no_likes_or_views_column():
    df = pd.DataFrame({'Title': ['Video 1', 'Video 2', 'Video 3']})
    ax = task_func(df)
    assert ax.get_figure().get_axes() == []

def test_task_func_no_interesting_videos():
    df = pd.DataFrame({'Title': ['Video 1', 'Video 2', 'Video 3'], 'Likes': [10, 20, 30], 'Views': [100, 200, 300]})
    ax = task_func(df)
    assert ax.get_figure().get_axes() == []

def test_task_func_interesting_videos():
    df = pd.DataFrame({'Title': ['Video 1', 'Video 2', 'Video 3'], 'Likes': [10, 20, 30], 'Views': [100, 200, 300]})
    ax = task_func(df)
    assert ax.get_figure().get_axes() == [ax]
    assert ax.get_ylabel() == 'Like Ratio'
    assert ax.get_xticklabels() == ['Video 1', 'Video 2', 'Video 3']
    assert ax.get_xticklabels_rotation() == 90