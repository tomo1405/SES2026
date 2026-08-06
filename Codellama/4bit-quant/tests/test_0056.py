import pandas as pd
from src_0056 import task_func


def test_task_func():
    text = "This is a sample text. It has multiple sentences."
    expected_output = pd.Series({"Sentence 1": 3, "Sentence 2": 4})
    assert task_func(text) == expected_output

def test_task_func_with_stopwords():
    text = "These are the words to ignore. They should not be counted."
    expected_output = pd.Series({"Sentence 1": 4})
    assert task_func(text) == expected_output

def test_task_func_with_empty_string():
    text = ""
    expected_output = pd.Series()
    assert task_func(text) == expected_output

def test_task_func_with_single_sentence():
    text = "This is a single sentence."
    expected_output = pd.Series({"Sentence 1": 4})
    assert task_func(text) == expected_output