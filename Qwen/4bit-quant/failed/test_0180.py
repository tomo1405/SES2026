import pytest
from src_0180 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {
        'Title': ['How to learn Python', 'What is Machine Learning', 'Introduction to AI'],
        'Content': [
            'Python is a great language for data science.',
            'Machine learning is a subset of artificial intelligence.',
            'AI involves building intelligent machines.'
        ]
    }
    return pd.DataFrame(data)

def test_task_func_with_valid_data(sample_df):
    ax = task_func(sample_df)
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) > 0, "No bars in the plot"

def test_task_func_with_no_matching_titles(sample_df):
    sample_df['Title'] = ['No match here', 'Another non-match']
    ax = task_func(sample_df)
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 0, "There should be no bars in the plot"

def test_task_func_with_missing_columns():
    sample_df = sample_df[['Title']]  # Remove 'Content' column
    ax = task_func(sample_df)
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 0, "There should be no bars in the plot"

def test_task_func_with_empty_dataframe():
    df = pd.DataFrame(columns=['Title', 'Content'])
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 0, "There should be no bars in the plot"