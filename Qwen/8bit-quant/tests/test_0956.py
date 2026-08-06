from collections import Counter

import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_0956 import task_func


def test_task_func_empty_text():
    with pytest.raises(ValueError):
        task_func(["hello", "world"], "")

def test_task_func_no_substitution():
    mystrings = ["hello", "world"]
    text = "This is a test text."
    ax = task_func(mystrings, text)
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    words, frequencies = zip(*Counter(text.split()).items())
    indices = np.arange(len(word_counts))
    
    # Check if the x-ticks and labels are set correctly
    assert list(ax.get_xticks()) == list(indices)
    assert list(ax.get_xticklabels()) == list(words)
    
    # Check if the bar heights are correct
    bars = ax.patches
    for bar, freq in zip(bars, frequencies):
        assert bar.get_height() == freq

def test_task_func_with_substitution():
    mystrings = ["hello world"]
    text = "Hello World is a test text."
    ax = task_func(mystrings, text)
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    words, frequencies = zip(*Counter(text.replace(" ", "_").split("_")).items())
    indices = np.arange(len(word_counts))
    
    # Check if the x-ticks and labels are set correctly
    assert list(ax.get_xticks()) == list(indices)
    assert list(ax.get_xticklabels()) == list(words)
    
    # Check if the bar heights are correct
    bars = ax.patches
    for bar, freq in zip(bars, frequencies):
        assert bar.get_height() == freq

def test_task_func_case_insensitivity():
    mystrings = ["HELLO world"]
    text = "hello World is a test text."
    ax = task_func(mystrings, text)
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    words, frequencies = zip(*Counter(text.replace(" ", "_").split("_")).items())
    indices = np.arange(len(word_counts))
    
    # Check if the x-ticks and labels are set correctly
    assert list(ax.get_xticks()) == list(indices)
    assert list(ax.get_xticklabels()) == list(words)
    
    # Check if the bar heights are correct
    bars = ax.patches
    for bar, freq in zip(bars, frequencies):
        assert bar.get_height() == freq