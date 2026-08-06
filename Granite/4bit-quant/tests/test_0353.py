import pandas as pd
import pytest
from src_0353 import task_func


def test_task_func():
    text_dict = {'apple': 10, 'banana': 5, 'cherry': 3, 'date': 2, 'elderberry': 1}
    word_keys = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    top_k = 3

    ax, top_words = task_func(text_dict, word_keys, top_k)

    assert isinstance(ax, pd.Series)
    assert isinstance(top_words, dict)
    assert len(top_words) == top_k
    assert all(word in text_dict for word in top_words)

def test_task_func_invalid_top_k():
    text_dict = {'apple': 10, 'banana': 5, 'cherry': 3, 'date': 2, 'elderberry': 1}
    word_keys = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    top_k = -1

    with pytest.raises(ValueError):
        task_func(text_dict, word_keys, top_k)

def test_task_func_top_k_greater_than_len_text_dict():
    text_dict = {'apple': 10, 'banana': 5, 'cherry': 3, 'date': 2, 'elderberry': 1}
    word_keys = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    top_k = len(text_dict) + 1

    ax, top_words = task_func(text_dict, word_keys, top_k)

    assert isinstance(ax, pd.Series)
    assert isinstance(top_words, dict)
    assert len(top_words) == len(text_dict)
    assert all(word in text_dict for word in top_words)