import pandas as pd
import pytest
from src_0176 import task_func

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'Likes': [100, 200, 300, 400, 500],
        'Views': [1000, 2000, 3000, 4000, 5000],
        'Title': ['How to Train Your Dragon', 'How to Become a Player', 'How to Cook a Turkey', 'How to Draw a Unicorn', 'How to Write a Python Script']
    })

def test_task_func_with_empty_df(sample_df):
    empty_df = pd.DataFrame()
    ax = task_func(empty_df)
    assert ax.get_title() == 'Empty DataFrame'

def test_task_func_with_missing_columns(sample_df):
    missing_columns_df = sample_df.drop(['Likes', 'Views', 'Title'], axis=1)
    ax = task_func(missing_columns_df)
    assert ax.get_title() == 'Missing Required Columns'

def test_task_func_with_no_interesting_videos(sample_df):
    no_interesting_videos_df = sample_df.copy()
    no_interesting_videos_df['Title'] = ['Foo', 'Bar', 'Baz']
    ax = task_func(no_interesting_videos_df)
    assert ax.get_title() == 'No Interesting Videos'

def test_task_func_with_interesting_videos(sample_df):
    ax = task_func(sample_df)
    assert ax.get_title() == 'Like Ratio'
    assert ax.get_xlabel() == 'Title'
    assert ax.get_ylabel() == 'Like Ratio'
    assert len(ax.patches) == 5