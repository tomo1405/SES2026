import re
import matplotlib.pyplot as plt
import numpy as np
from src_0163 import task_func

def test_task_func():
    text = "This is a sample text for testing"
    ax = task_func(text)
    assert isinstance(ax, plt.Axes)  # Check if the returned value is an instance of plt.Axes
    assert ax.get_title() == "Distribution of Word Lengths"  # Check if the title is set correctly
    assert ax.get_xlabel() == "Word Length"  # Check if the x-label is set correctly
    assert ax.get_ylabel() == "Frequency"  # Check if the y-label is set correctly

def test_task_func_empty_text():
    text = ""
    ax = task_func(text)
    assert isinstance(ax, plt.Axes)  # Check if the returned value is an instance of plt.Axes
    assert len(ax.patches) == 0  # Check if the histogram is empty when there are no words in the text

def test_task_func_no_words():
    text = "This text contains no words"
    ax = task_func(text)
    assert isinstance(ax, plt.Axes)  # Check if the returned value is an instance of plt.Axes
    assert len(ax.patches) == 0  # Check if the histogram is empty when there are no words in the text