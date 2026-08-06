import pandas as pd
from src_0053 import task_func


def test_task_func_empty_string():
    result = task_func("")
    assert result.empty

def test_task_func_single_word():
    result = task_func("Hello")
    assert result.equals(pd.Series([1], index=['hello']))

def test_task_func_multiple_words():
    result = task_func("Hello world hello")
    assert result.equals(pd.Series([2], index=['hello']))

def test_task_func_with_stopwords():
    result = task_func("The quick brown fox jumps over the lazy dog")
    expected = pd.Series([1, 1, 1, 1, 1], index=['quick', 'brown', 'fox', 'jumps', 'over', 'lazy', 'dog'])
    assert result.equals(expected)

def test_task_func_case_insensitivity():
    result = task_func("HELLO hello")
    assert result.equals(pd.Series([2], index=['hello']))

def test_task_func_punctuation():
    result = task_func("Hello, world!")
    assert result.equals(pd.Series([1], index=['hello']))