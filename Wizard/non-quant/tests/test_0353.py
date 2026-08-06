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
    text_dict = {'apple': 10, 'banana': 5, 'orange': 20, 'pear': 15, 'grape': 10}
    word_keys = ['apple', 'banana', 'orange', 'pear', 'grape']
    ax, top_k_words = task_func(text_dict, word_keys)
    assert isinstance(ax, type(None))
    assert isinstance(top_k_words, dict)
    assert top_k_words == {'apple': 10, 'banana': 5}
    assert ax is None

def test_task_func_top_k():
    text_dict = {'apple': 10, 'banana': 5, 'orange': 20, 'pear': 15, 'grape': 10}
    word_keys = ['apple', 'banana', 'orange', 'pear', 'grape']
    ax, top_k_words = task_func(text_dict, word_keys, top_k=3)
    assert isinstance(ax, type(None))
    assert isinstance(top_k_words, dict)
    assert top_k_words == {'apple': 10, 'banana': 5, 'orange': 20}
    assert ax is None

def test_task_func_top_k_invalid():
    text_dict = {'apple': 10, 'banana': 5, 'orange': 20, 'pear': 15, 'grape': 10}
    word_keys = ['apple', 'banana', 'orange', 'pear', 'grape']
    with pytest.raises(ValueError):
        task_func(text_dict, word_keys, top_k=-1)

def test_task_func_top_k_greater_than_len():
    text_dict = {'apple': 10, 'banana': 5, 'orange': 20, 'pear': 15, 'grape': 10}
    word_keys = ['apple', 'banana', 'orange', 'pear', 'grape']
    ax, top_k_words = task_func(text_dict, word_keys, top_k=6)
    assert isinstance(ax, type(None))
    assert isinstance(top_k_words, dict)
    assert top_k_words == {'apple': 10, 'banana': 5, 'orange': 20, 'pear': 15, 'grape': 10}
    assert ax is None