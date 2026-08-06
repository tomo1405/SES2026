python
import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords

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

# Importing the required libraries
import pytest

# Testing the function with valid inputs
def test_task_func_valid_inputs():
    text = "This is a sample text for testing the task function"
    n = 2
    matrix_df, ax = task_func(text, n)
    assert isinstance(matrix_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)

# Testing the function with invalid inputs
def test_task_func_invalid_inputs():
    text = ""
    n = 2
    matrix_df, ax = task_func(text, n)
    assert isinstance(matrix_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)

# Running the tests
pytest.main(["-v", "--tb=line", "-rN", __file__])