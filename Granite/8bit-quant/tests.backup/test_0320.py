import re
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
from src_0320 import task_func
import pytest

def test_task_func():
    example_str = "This is an example string with words and frequencies [word1, 1], [word2, 2], [word3, 3]"
    top_n = 3

    ax, top_n_words = task_func(example_str, top_n)

    assert isinstance(ax, plt.Axes)
    assert isinstance(top_n_words, dict)
    assert len(top_n_words) == top_n
    assert all(isinstance(word, str) for word in top_n_words.keys())
    assert all(isinstance(count, int) for count in top_n_words.values())

def test_task_func_invalid_input():
    example_str = "This is an example string with words and frequencies [word1, 1], [word2, 2], [word3, 3]"
    top_n = -1

    with pytest.raises(ValueError):
        task_func(example_str, top_n)