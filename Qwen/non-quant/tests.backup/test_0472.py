import pytest
from src_0472 import task_func
from collections import Counter
import pandas as pd

def test_task_func_empty_list():
    result = task_func([])
    expected_df = pd.DataFrame(columns=["Count"])
    assert result.equals(expected_df)

def test_task_func_single_word():
    result = task_func(["Hello"])
    expected_df = pd.DataFrame({"Count": [1]}, index=["hello"])
    assert result.equals(expected_df)

def test_task_func_multiple_words():
    result = task_func(["Hello", "world", "HELLO", "World"])
    expected_df = pd.DataFrame({"Count": [2, 2]}, index=["hello", "world"])
    assert result.equals(expected_df)

def test_task_func_with_strip():
    result = task_func([" Hello ", " world "])
    expected_df = pd.DataFrame({"Count": [1, 1]}, index=["hello", "world"])
    assert result.equals(expected_df)

def test_task_func_with_counter():
    result = task_func(["apple", "banana", "Apple", "BANANA", "banana"])
    expected_df = pd.DataFrame({"Count": [1, 3]}, index=["apple", "banana"])
    assert result.equals(expected_df)