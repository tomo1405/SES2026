import pandas as pd
from src_0056 import task_func


def test_task_func_empty_string():
    input_text = ""
    expected_output = pd.Series()
    assert task_func(input_text).equals(expected_output)

def test_task_func_single_sentence():
    input_text = "This is a test sentence."
    expected_output = pd.Series({"Sentence 1": 3})
    assert task_func(input_text).equals(expected_output)

def test_task_func_multiple_sentences():
    input_text = "This is a test sentence. Another sentence here. And one more."
    expected_output = pd.Series({"Sentence 1": 3, "Sentence 2": 2, "Sentence 3": 2})
    assert task_func(input_text).equals(expected_output)

def test_task_func_with_stopwords():
    input_text = "Those are the words to ignore in this sentence."
    expected_output = pd.Series({"Sentence 1": 3})
    assert task_func(input_text).equals(expected_output)

def test_task_func_with_trailing_period():
    input_text = "This is a test sentence. "
    expected_output = pd.Series({"Sentence 1": 3})
    assert task_func(input_text).equals(expected_output)

def test_task_func_with_multiple_periods():
    input_text = "This is a test sentence.. Another sentence here... And one more."
    expected_output = pd.Series({"Sentence 1": 3, "Sentence 2": 2, "Sentence 3": 2})
    assert task_func(input_text).equals(expected_output)

def test_task_func_with_empty_sentences():
    input_text = ". . ."
    expected_output = pd.Series()
    assert task_func(input_text).equals(expected_output)