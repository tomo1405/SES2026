import re
import matplotlib.pyplot as plt
import numpy as np
from src_0163 import task_func
import pytest

def test_task_func():
    # Test case 1: Test with a string containing words
    text = "This is a sample text"
    ax = task_func(text)
    assert isinstance(ax, plt.Axes)  # Check if the returned object is an instance of plt.Axes
    assert ax.get_title() == "Distribution of Word Lengths"  # Check if the title is set correctly
    assert ax.get_xlabel() == "Word Length"  # Check if the x-label is set correctly
    assert ax.get_ylabel() == "Frequency"  # Check if the y-label is set correctly

    # Test case 2: Test with an empty string
    text = ""
    ax = task_func(text)
    assert isinstance(ax, plt.Axes)  # Check if the returned object is an instance of plt.Axes
    assert ax.get_title() == "Distribution of Word Lengths"  # Check if the title is set correctly
    assert ax.get_xlabel() == "Word Length"  # Check if the x-label is set correctly
    assert ax.get_ylabel() == "Frequency"  # Check if the y-label is set correctly

    # Test case 3: Test with a string containing only non-alphabetic characters
    text = "!!!"
    ax = task_func(text)
    assert isinstance(ax, plt.Axes)  # Check if the returned object is an instance of plt.Axes
    assert ax.get_title() == "Distribution of Word Lengths"  # Check if the title is set correctly
    assert ax.get_xlabel() == "Word Length"  # Check if the x-label is set correctly
    assert ax.get_ylabel() == "Frequency"  # Check if the y-label is set correctly