import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from src_1033 import task_func


def test_task_func_output():
    # Test with default parameters
    ax = task_func()
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object."

def test_task_func_empty_dataframe():
    # Test with rows=0 to simulate an empty DataFrame
    ax = task_func(rows=0)
    assert ax is None, "The function should return None if the DataFrame is empty."

def test_task_func_string_length():
    # Test with different string lengths
    ax = task_func(string_length=5)
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object with different string length."

def test_task_func_rows():
    # Test with different number of rows
    ax = task_func(rows=500)
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object with different number of rows."

def test_task_func_letter_frequency():
    # Test if the letter frequency is correctly computed
    ax = task_func(rows=10, string_length=2)
    df = pd.get_dummies(ax.get_figure().get_axes()[0].collections[0].get_offsets())
    assert df.shape[1] == 26, "The letter frequency DataFrame should have 26 columns (one for each letter)."

def test_task_func_correlation_matrix():
    # Test if the correlation matrix is correctly computed
    ax = task_func(rows=10, string_length=2)
    corr = ax.get_figure().get_axes()[0].collections[0].get_array()
    assert isinstance(corr, np.ndarray), "The correlation matrix should be a NumPy array."
    assert corr.shape[0] == 26 and corr.shape[1] == 26, "The correlation matrix should be 26x26."

def test_task_func_plot_annotation():
    # Test if the heatmap annotations are present
    ax = task_func(rows=10, string_length=2)
    texts = ax.get_figure().get_axes()[0].texts
    assert len(texts) > 0, "The heatmap should have annotations."