python
import pandas as pd
from collections import Counter
import pytest

def task_func(text_dict, word_keys, top_k=2):
    if top_k < 0:
        raise ValueError('top_k must be a positive integer.')
    elif top_k >= len(text_dict):
        top_k = len(text_dict)

    frequencies = [text_dict.get(word, 0) for word in word_keys]
    freq_dict = Counter(text_dict)
    top_k_words = freq_dict.most_common(top_k)
    word_series = pd.Series(frequencies, index=word_keys)
    ax = word_series.plot(kind='bar')
    return ax, dict(top_k_words)

def test_task_func():
    text_dict = {'apple': 5, 'banana': 3, 'orange': 2, 'pear': 1}
    word_keys = ['apple', 'banana', 'orange', 'pear']
    ax, top_k_words = task_func(text_dict, word_keys)
    assert isinstance(ax, type(None))
    assert isinstance(top_k_words, dict)
    assert len(top_k_words) == 2
    assert top_k_words['apple'] == 5
    assert top_k_words['banana'] == 3
    assert top_k_words['orange'] == 2
    assert top_k_words['pear'] == 1