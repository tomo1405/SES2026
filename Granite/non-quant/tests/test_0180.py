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
        'Title': ['How to cook', 'What is Python', 'How to sleep'],
        'Content': ['Learn to cook', 'Python is a programming language', 'Sleep is important']
    })

def test_task_func_with_interesting_articles(sample_df):
    ax = task_func(sample_df)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_no_interesting_articles(sample_df):
    sample_df = pd.DataFrame({
        'Title': ['How to cook', 'What is Python', 'Sleep is important'],
        'Content': ['Learn to cook', 'Python is a programming language', 'Sleep is important']
    })
    ax = task_func(sample_df)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_missing_columns(sample_df):
    sample_df = sample_df.drop('Title', axis=1)
    with pytest.raises(ValueError, match=r'The DataFrame must have the columns'):
        task_func(sample_df)