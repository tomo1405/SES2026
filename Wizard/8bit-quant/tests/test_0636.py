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

# Testing the function
def test_task_func():
    # Test case 1: Valid input
    text = "The quick brown fox jumps over the lazy dog"
    n = 2
    expected_matrix_df = pd.DataFrame(data=[[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]],
                                       index=['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'lazy', 'dog', 'quick brown', 'brown fox'],
                                       columns=['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'lazy', 'dog', 'quick brown', 'brown fox'])
    expected_ax = plt.Axes(plt.figure(), [0., 0., 1., 1.])
    expected_ax.set_axis_off()
    expected_ax.set_title('Co-occurrence Matrix')
    expected_ax.set_xlabel('Word')
    expected_ax.set_ylabel('Word')
    expected_ax.imshow(expected_matrix_df, cmap='hot')
    expected_ax.set_xticks(np.arange(len(expected_matrix_df.columns)))
    expected_ax.set_yticks(np.arange(len(expected_matrix_df.index)))
    expected_ax.set_xticklabels(expected_matrix_df.columns, rotation=90)
    expected_ax.set_yticklabels(expected_matrix_df.index)
    expected_ax.tick_params(axis='both', which='both', length=0)
    expected_ax.grid(False)
    expected_ax.set_aspect('equal')

    matrix_df, ax = task_func(text, n)
    assert matrix_df.equals(expected_matrix_df)
    assert ax.figure.axes[0].equals(expected_ax)

    # Test case 2: Empty input
    text = ""
    n = 2
    expected_matrix_df = pd.DataFrame()
    expected_ax = plt.Axes(plt.figure(), [0., 0., 1., 1.])
    expected_ax.set_axis_off()
    expected_ax.set_title('Co-occurrence Matrix')
    expected_ax.set_xlabel('Word')
    expected_ax.set_ylabel('Word')
    expected_ax.imshow(expected_matrix_df, cmap='hot')
    expected_ax.set_xticks([])
    expected_ax.set_yticks([])
    expected_ax.tick_params(axis='both', which='both', length=0)
    expected_ax.grid(False)
    expected_ax.set_aspect('equal')

    matrix_df, ax = task_func(text, n)
    assert matrix_df.equals(expected_matrix_df)
    assert ax.figure.axes[0].equals(expected_ax)

    # Test case 3: Invalid input
    text = "The quick brown fox jumps over the lazy dog"
    n = 3
    with pytest.raises(ValueError):
        matrix_df, ax = task_func(text, n)

test_task_func()