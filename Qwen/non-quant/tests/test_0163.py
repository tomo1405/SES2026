import pytest
from src_0163 import task_func
import matplotlib.pyplot as plt
import numpy as np

def test_task_func_no_words():
    ax = task_func("")
    assert isinstance(ax, plt.Axes)
    assert ax.get_lines() == [], "No lines should be plotted for empty input"
    assert ax.get_title() == "Distribution of Word Lengths"
    assert ax.get_xlabel() == "Word Length"
    assert ax.get_ylabel() == "Frequency"

def test_task_func_single_word():
    ax = task_func("hello")
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 1, "One bar should be plotted for one word"
    assert ax.patches[0].get_height() == 1, "The frequency of the word should be 1"
    assert ax.patches[0].get_width() == 1, "The width of the bar should be the length of the word"
    assert ax.get_title() == "Distribution of Word Lengths"
    assert ax.get_xlabel() == "Word Length"
    assert ax.get_ylabel() == "Frequency"

def test_task_func_multiple_words():
    ax = task_func("hello world this is a test")
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) > 1, "More than one bar should be plotted for multiple words"
    assert ax.get_title() == "Distribution of Word Lengths"
    assert ax.get_xlabel() == "Word Length"
    assert ax.get_ylabel() == "Frequency"

def test_task_func_special_characters():
    ax = task_func("hello, world! this-is_a_test.")
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) > 1, "More than one bar should be plotted for multiple words"
    assert ax.get_title() == "Distribution of Word Lengths"
    assert ax.get_xlabel() == "Word Length"
    assert ax.get_ylabel() == "Frequency"

def test_task_func_rwidth_parameter():
    ax = task_func("hello", rwidth=0.5)
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 1, "One bar should be plotted for one word"
    assert ax.patches[0].get_width() == 0.5, "The width of the bar should be affected by rwidth parameter"
    assert ax.get_title() == "Distribution of Word Lengths"
    assert ax.get_xlabel() == "Word Length"
    assert ax.get_ylabel() == "Frequency"