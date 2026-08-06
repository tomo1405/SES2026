import pytest
import pandas as pd
from src_0176 import task_func

@pytest.fixture
def df():
    return pd.DataFrame({
        'Likes': [100, 200, 300, 400, 500],
        'Views': [1000, 2000, 3000, 4000, 5000],
        'Title': ['How to Train Your Dragon', 'What is Python', 'How to Eat an Elephant', 'What is Machine Learning', 'How to Code a Video Game']
    })

def test_task_func_with_empty_df(df):
    df_empty = pd.DataFrame()
    ax = task_func(df_empty)
    assert ax.get_title() == 'Empty DataFrame'

def test_task_func_with_missing_columns(df):
    df_missing_columns = df.drop(columns=['Likes', 'Views', 'Title'])
    ax = task_func(df_missing_columns)
    assert ax.get_title() == 'Missing required columns'

def test_task_func_with_no_interesting_videos(df):
    df_no_interesting_videos = df.copy()
    df_no_interesting_videos['Title'] = 'No Interesting Videos'
    ax = task_func(df_no_interesting_videos)
    assert ax.get_title() == 'No interesting videos found'

def test_task_func_with_interesting_videos(df):
    ax = task_func(df)
    expected_title = 'Like Ratio'
    expected_xlabel = 'Title'
    expected_ylabel = 'Like Ratio'
    assert ax.get_title() == expected_title
    assert ax.get_xlabel() == expected_xlabel
    assert ax.get_ylabel() == expected_ylabel