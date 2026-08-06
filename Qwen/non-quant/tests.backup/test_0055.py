import pytest
from src_0055 import task_func
import pandas as pd
import numpy as np

def test_task_func_with_empty_string():
    result = task_func("")
    assert result.empty

def test_task_func_with_single_sentence():
    text = "This is a test sentence."
    result = task_func(text)
    expected_columns = ["this", "is", "a", "test", "sentence"]
    assert list(result.columns) == expected_columns
    assert result.shape == (1, len(expected_columns))

def test_task_func_with_multiple_sentences():
    text = "This is the first sentence. This is the second sentence."
    result = task_func(text)
    expected_columns = ["this", "is", "the", "first", "sentence", "second"]
    assert list(result.columns) == expected_columns
    assert result.shape == (2, len(expected_columns))

def test_task_func_with_trailing_period():
    text = "This is a test sentence. "
    result = task_func(text)
    expected_columns = ["this", "is", "a", "test", "sentence"]
    assert list(result.columns) == expected_columns
    assert result.shape == (1, len(expected_columns))

def test_task_func_with_no_periods():
    text = "This is a test sentence"
    result = task_func(text)
    expected_columns = ["this", "is", "a", "test", "sentence"]
    assert list(result.columns) == expected_columns
    assert result.shape == (1, len(expected_columns))

def test_task_func_with_special_characters():
    text = "Hello, world! How are you?"
    result = task_func(text)
    expected_columns = ["hello", "world", "how", "are", "you"]
    assert list(result.columns) == expected_columns
    assert result.shape == (2, len(expected_columns))

def test_task_func_with_numbers():
    text = "I have 2 apples and 3 bananas."
    result = task_func(text)
    expected_columns = ["i", "have", "apples", "and", "bananas"]
    assert list(result.columns) == expected_columns
    assert result.shape == (1, len(expected_columns))