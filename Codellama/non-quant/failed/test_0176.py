import pytest
from src_0176 import task_func

def test_task_func_empty_df():
    df = pd.DataFrame()
    ax = task_func(df)
    assert ax is not None

def test_task_func_no_likes_views_title():
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
    ax = task_func(df)
    assert ax is not None

def test_task_func_no_interesting_videos():
    df = pd.DataFrame({'Title': ['video1', 'video2', 'video3'], 'Likes': [10, 20, 30], 'Views': [100, 200, 300]})
    ax = task_func(df)
    assert ax is not None

def test_task_func_interesting_videos():
    df = pd.DataFrame({'Title': ['video1', 'video2', 'video3'], 'Likes': [10, 20, 30], 'Views': [100, 200, 300]})
    ax = task_func(df)
    assert ax is not None
    assert ax.get_ylabel() == 'Like Ratio'
    assert ax.get_xticklabels() == ['video1', 'video2', 'video3']
    assert ax.get_xticklabels_rotation() == 90