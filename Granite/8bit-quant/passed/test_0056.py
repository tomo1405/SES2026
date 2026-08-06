import re
import pandas as pd
from src_0056 import task_func
import pytest

def test_task_func():
    text = "This is a sample text. It contains multiple sentences. Those are the words to ignore."
    expected_output = pd.Series({"Sentence 1": 4, "Sentence 2": 5})

    actual_output = task_func(text)

    assert actual_output.equals(expected_output)

def test_task_func_with_empty_text():
    text = ""
    expected_output = pd.Series()

    actual_output = task_func(text)

    assert actual_output.equals(expected_output)

def test_task_func_with_no_sentences():
    text = "This text contains no sentences."
    expected_output = pd.Series()

    actual_output = task_func(text)

    assert actual_output.equals(expected_output)