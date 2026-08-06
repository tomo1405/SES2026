import pytest
from src_0353 import task_func

def test_task_func():
    text_dict = {'hello': 10, 'world': 5, 'python': 3, 'testing': 2}
    word_keys = ['hello', 'world', 'python', 'testing']
    top_k = 2

    ax, top_k_words = task_func(text_dict, word_keys, top_k)

    assert isinstance(ax, pd.Series)
    assert isinstance(top_k_words, dict)
    assert len(top_k_words) == top_k
    assert all(word in word_keys for word in top_k_words.keys())
    assert all(isinstance(freq, int) for freq in top_k_words.values())
    assert all(freq >= 0 for freq in top_k_words.values())