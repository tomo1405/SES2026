import re
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd
import pytest

from src_0180 import task_func

@pytest.fixture
def df():
    return pd.DataFrame({
        'Title': ['How to Train Your Dragon', 'Harry Potter and the Philosopher\'s Stone', 'The Hobbit'],
        'Content': [' dragon training methods', 'harry potter books', 'hobbit movies']
    })

def test_task_func_with_valid_input(df):
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_invalid_input(df):
    df = df.drop('Title', axis=1)
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_with_no_interesting_articles(df):
    df = pd.DataFrame({
        'Title': ['Alice in Wonderland', 'The Adventures of Sherlock Holmes', 'Pride and Prejudice'],
        'Content': ['Alice books', 'Sherlock Holmes books', 'Pride and Prejudice books']
    })
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_invalid_pattern(df):
    df = pd.DataFrame({
        'Title': ['How to Train Your Dragon', 'Harry Potter and the Philosopher\'s Stone', 'The Hobbit'],
        'Content': ['dragon training methods', 'harry potter books', 'hobbit movies']
    })
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)