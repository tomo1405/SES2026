import pytest
from src_0176 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import re

# Sample data for testing
data = {
    'Title': ['Video1', 'Video2', 'Video3'],
    'Likes': [10, 20, 30],
    'Views': [100, 200, 300]
}
df = pd.DataFrame(data)

def test_task_func():
    # Test when df is empty
    empty_df = pd.DataFrame(columns=['Title', 'Likes', 'Views'])
    assert task_func(empty_df) is None

    # Test when 'Likes' or 'Views' or 'Title' columns are missing
    df_missing_columns = pd.DataFrame(data)
    df_missing_columns.drop(columns=['Likes', 'Views', 'Title'], inplace=True)
    assert task_func(df_missing_columns) is None

    # Test when there are no interesting videos
    df_no_interesting_videos = pd.DataFrame(data)
    assert task_func(df_no_interesting_videos) is None

    # Test when there are interesting videos
    result = task_func(df)
    assert isinstance(result, plt.Axes)
    plt.close()  # Close the plot to avoid hanging tests