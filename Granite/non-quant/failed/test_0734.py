import re
import string
from src_0734 import task_func
import pytest

def test_task_func():
    assert task_func("Hello world!") == 2
    assert task_func("This is a test.") == 3
    assert task_func("I am testing this function.") == 6
    assert task_func("stopword is a stopword.") == 0
    assert task_func("This is a test with a stopword.") == 4

def test_task_func_with_punctuation():
    assert task_func("Hello, world!") == 2
    assert task_func("This is a test...") == 3
    assert task_func("I'm testing this function.") == 6
    assert task_func("stopword, is a stopword.") == 0
    assert task_func("This is a test with a stopword,") == 4

def test_task_func_with_stopwords():
    assert task_func("This is a test with stopwords.") == 2
    assert task_func("This is a test with stopwords in it.") == 3
    assert task_func("This is a test with stopwords in it and more stopwords.") == 4
    assert task_func("This is a test with stopwords in it and more stopwords in it.") == 5

def test_task_func_with_empty_string():
    assert task_func("") == 0
    assert task_func(" ") == 0
    assert task_func("        ") == 0

def test_task_func_with_invalid_input():
    with pytest.raises(TypeError):
        task_func(123)
    with pytest.raises(TypeError):
        task_func([1, 2, 3])
    with pytest.raises(TypeError):
        task_func({"a": 1, "b": 2})