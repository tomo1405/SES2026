import pandas as pd
from src_0176 import task_func


def test_task_func_empty_df():
    df = pd.DataFrame()
    ax = task_func(df)
    assert ax is not None

def test_task_func_no_interesting_videos():
    df = pd.DataFrame({'Likes': [10, 20, 30], 'Views': [100, 200, 300], 'Title': ['video 1', 'video 2', 'video 3']})
    ax = task_func(df)
    assert ax is not None

def test_task_func_interesting_videos():
    df = pd.DataFrame({'Likes': [10, 20, 30], 'Views': [100, 200, 300], 'Title': ['video 1', 'video 2', 'video 3']})
    ax = task_func(df)
    assert ax is not None
    assert ax.get_ylabel() == 'Like Ratio'
    assert ax.get_xticklabels() == ['video 1', 'video 2', 'video 3']
    assert ax.get_xticklabels(rotation='vertical') == ['video 1', 'video 2', 'video 3']