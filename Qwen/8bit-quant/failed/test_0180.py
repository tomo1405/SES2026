import pytest
from src_0180 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer

# Mock data for testing
def create_mock_df():
    data = {
        'Title': ['How to learn Python', 'What is AI?', 'Introduction to Data Science'],
        'Content': [
            'Python is a versatile programming language.',
            'AI stands for Artificial Intelligence.',
            'Data Science involves analyzing and interpreting data.'
        ]
    }
    return pd.DataFrame(data)

def test_task_func_no_required_columns():
    df = pd.DataFrame({'Title': ['Test Title'], 'Description': ['Test Description']})
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)

def test_task_func_no_interesting_articles():
    df = pd.DataFrame({
        'Title': ['Not relevant title', 'Another uninteresting title'],
        'Content': ['Irrelevant content', 'More irrelevant content']
    })
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_interesting_articles():
    df = create_mock_df()
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) > 0  # Check if there are bars in the plot

def test_task_func_tfidf_scores():
    df = create_mock_df()
    ax = task_func(df)
    assert len(ax.patches) == len(TfidfVectorizer().fit_transform(df['Content']).get_feature_names_out())

def test_task_func_labels_and_ticks():
    df = create_mock_df()
    ax = task_func(df)
    assert ax.get_ylabel() == 'TF-IDF Score'
    assert all([tick.get_rotation() == 'vertical' for tick in ax.get_xticklabels()])