import pandas as pd
import pytest
import regex as re
from src_0053 import task_func

# Constants
STOPWORDS = ["a", "an", "the", "in", "is", "are"]

def test_task_func():
    text = "This is a sample text."
    expected_result = pd.Series(["sample", "text."])
    result = task_func(text)
    assert result.equals(expected_result)

def test_task_func_with_stopwords():
    text = "This is a sample text."
    expected_result = pd.Series(["sample", "text."])
    result = task_func(text)
    assert result.equals(expected_result)

def test_task_func_with_empty_text():
    text = ""
    expected_result = pd.Series([])
    result = task_func(text)
    assert result.equals(expected_result)

def test_task_func_with_no_stopwords():
    text = "This is a sample text with no stopwords."
    expected_result = pd.Series(["sample", "text", "no", "stopwords."])
    result = task_func(text)
    assert result.equals(expected_result)