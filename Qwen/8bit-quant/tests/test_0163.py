import pytest
from src_0163 import task_func
import matplotlib.pyplot as plt
import numpy as np

def test_task_func_with_empty_text():
    ax = task_func("")
    assert len(ax.patches) == 0  # No bars should be plotted for empty text

def test_task_func_with_single_word():
    ax = task_func("hello")
    assert len(ax.patches) == 1  # One bar should be plotted for one word
    assert ax.patches[0].get_height() == 1  # Frequency of word length 5 is 1

def test_task_func_with_multiple_words():
    ax = task_func("hello world")
    assert len(ax.patches) == 2  # Two bars should be plotted for two words
    word_lengths = [patch.get_width() for patch in ax.patches]
    frequencies = [patch.get_height() for patch in ax.patches]
    assert sorted(word_lengths) == [5, 5]  # Both words have length 5
    assert frequencies == [1, 1]  # Each word appears once

def test_task_func_with_punctuation():
    ax = task_func("hello, world!")
    assert len(ax.patches) == 2  # Two bars should be plotted for two words
    word_lengths = [patch.get_width() for patch in ax.patches]
    frequencies = [patch.get_height() for patch in ax.patches]
    assert sorted(word_lengths) == [5, 5]  # Both words have length 5
    assert frequencies == [1, 1]  # Each word appears once

def test_task_func_with_rwidth():
    ax = task_func("hello", rwidth=0.5)
    assert len(ax.patches) == 1  # One bar should be plotted for one word
    assert ax.patches[0].get_width() == 0.5  # rwidth should affect the bar width

def test_task_func_with_no_words():
    ax = task_func("!!!")
    assert len(ax.patches) == 0  # No bars should be plotted for no valid words

def test_task_func_with_large_text():
    ax = task_func("a" * 100 + " b" * 100)
    assert len(ax.patches) == 2  # Two bars should be plotted for two different word lengths
    word_lengths = [patch.get_width() for patch in ax.patches]
    frequencies = [patch.get_height() for patch in ax.patches]
    assert sorted(word_lengths) == [1, 2]  # Word lengths are 1 and 2
    assert frequencies == [100, 100]  # Each word length appears 100 times

def test_task_func_with_whitespace():
    ax = task_func("   ")
    assert len(ax.patches) == 0  # No bars should be plotted for only whitespace