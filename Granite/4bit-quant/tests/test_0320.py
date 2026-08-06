import re
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
from src_0320 import task_func

def test_task_func():
    example_str = "This is an example string with some words and a frequency distribution[word1, word2, word3]"
    ax, top_n_words = task_func(example_str)
    assert isinstance(ax, plt.Axes)
    assert isinstance(top_n_words, dict)
    assert len(top_n_words) == 30
    assert "word1" in top_n_words and "word2" in top_n_words and "word3" in top_n_words

def test_task_func_with_top_n():
    example_str = "This is an example string with some words and a frequency distribution[word1, word2, word3]"
    ax, top_n_words = task_func(example_str, top_n=2)
    assert isinstance(ax, plt.Axes)
    assert isinstance(top_n_words, dict)
    assert len(top_n_words) == 2
    assert "word1" in top_n_words and "word2" in top_n_words