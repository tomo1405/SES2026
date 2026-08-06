import pytest
from src_1005 import task_func

def test_task_func():
    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    word_freq, ax = task_func(url)
    assert isinstance(word_freq, dict)
    assert ax.get_title() == "Top 10 Most Common Words"
    assert ax.get_xlabel() == "Words"
    assert ax.get_ylabel() == "Frequency"