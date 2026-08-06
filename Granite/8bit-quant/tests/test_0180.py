import re
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd
import pytest

from src_0180 import task_func

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'Title': ['How to cook', 'What is Python', 'How to play chess'],
        'Content': ['Learn to cook by following the recipe', 'Python is a popular programming language', 'Learn to play chess by reading a book']
    })

def test_task_func_with_interesting_articles(sample_df):
    ax = task_func(sample_df)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_no_interesting_articles(sample_df):
    sample_df['Title'] = ['Learn to swim', 'Learn to read', 'Learn to dance']
    ax = task_func(sample_df)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_missing_columns(sample_df):
    sample_df.drop(columns=['Title', 'Content'], inplace=True)
    with pytest.raises(KeyError):
        task_func(sample_df)