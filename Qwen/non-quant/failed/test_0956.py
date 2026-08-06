import pytest
from src_0956 import task_func
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def test_task_func_empty_text():
    with pytest.raises(ValueError):
        task_func(["test"], "")

def test_task_func_no_replacement():
    ax = task_func(["not_in_text"], "This is a test text.")
    words, frequencies = zip(*Counter("This is a test text.".split()).items())
    indices = np.arange(len(Counter("This is a test text.".split())))
    assert list(ax.get_xticks()) == list(indices)
    assert list(ax.get_xticklabels()) == list(words)
    assert list(ax.patches[0].get_height()) == [frequencies[0]]

def test_task_func_with_replacement():
    ax = task_func(["is"], "This is a test text.")
    words, frequencies = zip(*Counter("This_is a test text.".split()).items())
    indices = np.arange(len(Counter("This_is a test text.".split())))
    assert list(ax.get_xticks()) == list(indices)
    assert list(ax.get_xticklabels()) == list(words)
    assert list(ax.patches[0].get_height()) == [frequencies[0]]

def test_task_func_case_insensitive():
    ax = task_func(["TEST"], "This is a TEST text.")
    words, frequencies = zip(*Counter("This is a TEST_text.".split()).items())
    indices = np.arange(len(Counter("This is a TEST_text.".split())))
    assert list(ax.get_xticks()) == list(indices)
    assert list(ax.get_xticklabels()) == list(words)
    assert list(ax.patches[0].get_height()) == [frequencies[0]]