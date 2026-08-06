import pytest
from src_0320 import task_func

def test_task_func():
    example_str = "This is an example string [1234567890]"
    ax, top_n_words = task_func(example_str, top_n=30)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert isinstance(top_n_words, dict)
    assert len(top_n_words) == 30
    assert all(isinstance(word, str) for word in top_n_words.keys())
    assert all(isinstance(count, int) for count in top_n_words.values())