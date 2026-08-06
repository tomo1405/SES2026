import matplotlib
from src_0320 import task_func


def test_task_func():
    example_str = '[1, 2, 3, 4, 5]'
    top_n = 30
    ax, top_n_words = task_func(example_str, top_n)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert isinstance(top_n_words, dict)
    assert len(top_n_words) == top_n
    assert all(isinstance(word, str) for word in top_n_words.keys())
    assert all(isinstance(count, int) for count in top_n_words.values())