import pytest
from src_0353 import task_func
from collections import Counter
import pandas as pd

def test_task_func_basic():
    text_dict = {'apple': 4, 'banana': 2, 'cherry': 7}
    word_keys = ['apple', 'banana', 'cherry']
    ax, top_k_words = task_func(text_dict, word_keys)
    assert isinstance(ax, pd.Series)
    assert top_k_words == [('cherry', 7), ('apple', 4)]

def test_task_func_top_k_less_than_length():
    text_dict = {'apple': 4, 'banana': 2, 'cherry': 7, 'date': 1}
    word_keys = ['apple', 'banana', 'cherry', 'date']
    ax, top_k_words = task_func(text_dict, word_keys, top_k=2)
    assert top_k_words == [('cherry', 7), ('apple', 4)]

def test_task_func_top_k_greater_than_length():
    text_dict = {'apple': 4, 'banana': 2}
    word_keys = ['apple', 'banana']
    ax, top_k_words = task_func(text_dict, word_keys, top_k=5)
    assert top_k_words == [('apple', 4), ('banana', 2)]

def test_task_func_negative_top_k():
    text_dict = {'apple': 4, 'banana': 2}
    word_keys = ['apple', 'banana']
    with pytest.raises(ValueError):
        task_func(text_dict, word_keys, top_k=-1)

def test_task_func_missing_word_keys():
    text_dict = {'apple': 4, 'banana': 2}
    word_keys = ['apple', 'orange']
    ax, top_k_words = task_func(text_dict, word_keys)
    assert top_k_words == [('apple', 4), ('banana', 2)]
    assert ax['orange'] == 0

def test_task_func_empty_text_dict():
    text_dict = {}
    word_keys = ['apple', 'banana']
    ax, top_k_words = task_func(text_dict, word_keys)
    assert top_k_words == []
    assert ax['apple'] == 0
    assert ax['banana'] == 0