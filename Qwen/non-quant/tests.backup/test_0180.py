import pytest
from src_0180 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer

def test_task_func_no_required_columns():
    df = pd.DataFrame({'Title': ['How to cook'], 'Description': ['Recipe for cooking']})
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)

def test_task_func_no_interesting_articles():
    df = pd.DataFrame({'Title': ['Not interesting title'], 'Content': ['Not interesting content']})
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 0

def test_task_func_with_interesting_articles():
    df = pd.DataFrame({
        'Title': ['How to cook', 'What is cooking'],
        'Content': ['Recipe for cooking', 'Explanation of cooking']
    })
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) > 0

def test_task_func_tfidf_scores():
    df = pd.DataFrame({
        'Title': ['How to cook', 'What is cooking'],
        'Content': ['Recipe for cooking', 'Explanation of cooking']
    })
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    feature_names = ax.get_xticklabels()
    assert len(feature_names) > 0
    for label in feature_names:
        assert isinstance(label, plt.Text)

def test_task_func_plot_labels():
    df = pd.DataFrame({
        'Title': ['How to cook', 'What is cooking'],
        'Content': ['Recipe for cooking', 'Explanation of cooking']
    })
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    assert ax.get_ylabel() == 'TF-IDF Score'
    assert plt.xticks(rotation='vertical') is not None