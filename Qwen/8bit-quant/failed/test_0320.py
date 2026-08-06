import pytest
from src_0320 import task_func
import matplotlib.pyplot as plt
from nltk.probability import FreqDist

def test_task_func():
    example_str = "This is a test [example] string with some repeated words words"
    top_n = 5

    ax, top_n_words = task_func(example_str, top_n)

    # Check if the returned object is a matplotlib AxesSubplot
    assert isinstance(ax, plt.Axes)

    # Check if the top_n_words is a dictionary
    assert isinstance(top_n_words, dict)

    # Check if the number of items in top_n_words is equal to top_n
    assert len(top_n_words) == top_n

    # Check if the most common words are correctly identified
    expected_top_words = {'words': 2, 'This': 1, 'is': 1, 'a': 1, 'test': 1}
    assert top_n_words == expected_top_words

    # Check if the plot is closed
    assert plt.fignum_exists(plt.gcf().number) is False