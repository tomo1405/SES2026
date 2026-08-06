import pytest
from src_1005 import task_func

def test_task_func():
    url = "https://www.python.org"
    word_freq, ax = task_func(url)
    assert isinstance(word_freq, Counter)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert len(word_freq) == 10
    assert ax.get_title() == "Top 10 Most Common Words"
    assert ax.get_xlabel() == "Words"
    assert ax.get_ylabel() == "Frequency"