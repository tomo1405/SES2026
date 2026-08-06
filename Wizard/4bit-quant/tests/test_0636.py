python
import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import pytest

def task_func(text, n=2):
    # Pre-processing the text
    # Remove duplicate consecutive words
    text = re.sub(r'\b(\w+)( \1\b)+', r'\1', text)
    stop_words = set(stopwords.words('english'))
    # Remove stopwords
    words_filtered = ' '.join([word for word in text.lower().split() if word not in stop_words])

    # If words_filtered is empty after removing stopwords, return an empty DataFrame
    if not words_filtered.strip():
        empty_df = pd.DataFrame()
        fig, ax = plt.subplots()
        return empty_df, ax

    # Generating co-occurrence matrix and plotting as before
    vectorizer = CountVectorizer(ngram_range=(n, n))
    X = vectorizer.fit_transform([words_filtered])  # Ensure input is treated as a single document
    matrix = (X.T * X).todense()
    np.fill_diagonal(matrix, 0)
    feature_names = vectorizer.get_feature_names_out() if hasattr(vectorizer, 'get_feature_names_out') else vectorizer.get_feature_names()
    matrix_df = pd.DataFrame(matrix, index=feature_names, columns=feature_names)

    fig, ax = plt.subplots()
    cax = ax.matshow(matrix_df, cmap='hot')
    fig.colorbar(cax)
    ax.set_xticks(np.arange(len(matrix_df.columns)))
    ax.set_yticks(np.arange(len(matrix_df.index)))
    ax.set_xticklabels(matrix_df.columns, rotation=90)
    ax.set_yticklabels(matrix_df.index)

    return matrix_df, ax

def test_task_func():
    # Test case 1: Valid input
    text = "The quick brown fox jumps over the lazy dog"
    n = 2
    matrix_df, ax = task_func(text, n)
    assert isinstance(matrix_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert matrix_df.shape == (10, 10)
    assert ax.get_xlabel() == "Word"
    assert ax.get_ylabel() == "Word"
    assert ax.get_title() == "Co-occurrence Matrix"

    # Test case 2: Empty input
    text = ""
    n = 2
    matrix_df, ax = task_func(text, n)
    assert isinstance(matrix_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert matrix_df.shape == (0, 0)
    assert ax.get_xlabel() == "Word"
    assert ax.get_ylabel() == "Word"
    assert ax.get_title() == "Co-occurrence Matrix"

    # Test case 3: Invalid input
    text = None
    n = 2
    with pytest.raises(TypeError):
        matrix_df, ax = task_func(text, n)