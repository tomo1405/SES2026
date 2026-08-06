import pandas as pd
from src_0056 import task_func


def test_task_func_empty_text():
    text = ""
    result = task_func(text)
    assert result.empty

def test_task_func_single_sentence():
    text = "This is a test sentence."
    result = task_func(text)
    expected = pd.Series({"Sentence 1": 4})
    pd.testing.assert_series_equal(result, expected)

def test_task_func_multiple_sentences():
    text = "This is a test sentence. Another sentence here. And one more."
    result = task_func(text)
    expected = pd.Series({"Sentence 1": 4, "Sentence 2": 3, "Sentence 3": 2})
    pd.testing.assert_series_equal(result, expected)

def test_task_func_with_stopwords():
    text = "Those are the words to ignore in this sentence."
    result = task_func(text)
    expected = pd.Series({"Sentence 1": 4})
    pd.testing.assert_series_equal(result, expected)

def test_task_func_with_punctuation():
    text = "Hello, world! How are you today?"
    result = task_func(text)
    expected = pd.Series({"Sentence 1": 2, "Sentence 2": 3})
    pd.testing.assert_series_equal(result, expected)

def test_task_func_with_empty_sentences():
    text = "First sentence. . . . Second sentence."
    result = task_func(text)
    expected = pd.Series({"Sentence 1": 2, "Sentence 2": 2})
    pd.testing.assert_series_equal(result, expected)