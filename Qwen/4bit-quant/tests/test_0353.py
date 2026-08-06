import pytest
from src_0353 import task_func
import pandas as pd
from collections import Counter

def test_task_func_positive_top_k():
    text_dict = {'apple': 5, 'banana': 3, 'cherry': 8}
    word_keys = ['apple', 'banana']
    top_k = 2
    ax, result = task_func(text_dict, word_keys, top_k)
    assert isinstance(ax, pd.plotting._matplotlib.bar.BarPlot)
    assert result == [('cherry', 8), ('apple', 5)]

def test_task_func_zero_top_k():
    text_dict = {'apple': 5, 'banana': 3, 'cherry': 8}
    word_keys = ['apple', 'banana']
    top_k = 0
    with pytest.raises(ValueError, match='top_k must be a positive integer.'):
        task_func(text_dict, word_keys, top_k)

def test_task_func_negative_top_k():
    text_dict = {'apple': 5, 'banana': 3, 'cherry': 8}
    word_keys = ['apple', 'banana']
    top_k = -1
    with pytest.raises(ValueError, match='top_k must be a positive integer.'):
        task_func(text_dict, word_keys, top_k)

def test_task_func_top_k_greater_than_dict_length():
    text_dict = {'apple': 5, 'banana': 3, 'cherry': 8}
    word_keys = ['apple', 'banana']
    top_k = 10
    ax, result = task_func(text_dict, word_keys, top_k)
    assert isinstance(ax, pd.plotting._matplotlib.bar.BarPlot)
    assert result == [('cherry', 8), ('apple', 5), ('banana', 3)]

def test_task_func_missing_word_key():
    text_dict = {'apple': 5, 'banana': 3, 'cherry': 8}
    word_keys = ['apple', 'orange']
    top_k = 2
    ax, result = task_func(text_dict, word_keys, top_k)
    assert isinstance(ax, pd.plotting._matplotlib.bar.BarPlot)
    assert result == [('cherry', 8), ('apple', 5)]