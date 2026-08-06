import pytest
from src_0176 import task_func
import pandas as pd
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {
        'Title': ['How to Code', 'What is Python', 'Random Video', 'Another Title'],
        'Likes': [100, 200, 50, 30],
        'Views': [500, 1000, 200, 100]
    }
    return pd.DataFrame(data)

def test_task_func_empty_df():
    df = pd.DataFrame()
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)

def test_task_func_missing_columns():
    df = pd.DataFrame({
        'Title': ['How to Code', 'What is Python'],
        'Likes': [100, 200]
    })
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)

def test_task_func_no_interesting_videos(sample_df):
    # Modify the 'Title' column to remove matches for the pattern
    sample_df['Title'] = ['No Match', 'Also No Match']
    ax = task_func(sample_df)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_interesting_videos(sample_df):
    ax = task_func(sample_df)
    assert isinstance(ax, plt.Axes)
    assert 'Like Ratio' in ax.get_ylabel()
    assert all(label.get_text() in sample_df['Title'] for label in ax.get_xticklabels())

def test_task_func_plot_content(sample_df):
    ax = task_func(sample_df)
    assert len(ax.patches) == 2  # Only two titles match the pattern
    assert ax.patches[0].get_height() == 100 / 500  # Like Ratio for 'How to Code'
    assert ax.patches[1].get_height() == 200 / 1000  # Like Ratio for 'What is Python'

def test_task_func_plot_rotation(sample_df):
    ax = task_func(sample_df)
    for label in ax.get_xticklabels():
        assert label.get_rotation() == 'vertical'