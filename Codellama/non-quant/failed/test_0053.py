import pytest
from src_0053 import task_func

def test_task_func():
    text = "The quick brown fox jumps over the lazy dog."
    expected_output = pd.Series(["quick", "brown", "fox", "jumps", "lazy", "dog"]).value_counts().rename(None)
    assert task_func(text) == expected_output

def test_task_func_with_stopwords():
    text = "The quick brown fox jumps over the lazy dog."
    expected_output = pd.Series(["quick", "brown", "fox", "jumps", "lazy", "dog"]).value_counts().rename(None)
    assert task_func(text) == expected_output

def test_task_func_with_empty_string():
    text = ""
    expected_output = pd.Series([]).value_counts().rename(None)
    assert task_func(text) == expected_output

def test_task_func_with_stopwords_only():
    text = "the in is a an"
    expected_output = pd.Series([]).value_counts().rename(None)
    assert task_func(text) == expected_output