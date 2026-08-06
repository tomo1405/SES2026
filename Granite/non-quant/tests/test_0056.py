import re
import pandas as pd
from src_0056 import task_func
import pytest

def test_task_func():
    text = "This is a sample text. It contains multiple sentences. Those are the words to ignore. Here's another sentence."
    expected_output = pd.Series({
        "Sentence 1": 5,
        "Sentence 2": 4,
        "Sentence 3": 5
    })
    actual_output = task_func(text)
    assert actual_output.equals(expected_output)

def test_task_func_empty_text():
    text = ""
    expected_output = pd.Series({})
    actual_output = task_func(text)
    assert actual_output.equals(expected_output)

def test_task_func_single_sentence():
    text = "This is a single sentence."
    expected_output = pd.Series({"Sentence 1": 4})
    actual_output = task_func(text)
    assert actual_output.equals(expected_output)