import pytest
from src_0728 import task_func
import numpy as np

def test_task_func_basic():
    input_string = "Test sentence"
    result = task_func(input_string)
    assert isinstance(result, np.ndarray)
    assert result.shape == (len(SENTENCES) + 1,)

def test_task_func_empty_string():
    input_string = ""
    result = task_func(input_string)
    assert isinstance(result, np.ndarray)
    assert result.shape == (len(SENTENCES) + 1,)

def test_task_func_special_characters():
    input_string = "Special #$% characters"
    result = task_func(input_string)
    assert isinstance(result, np.ndarray)
    assert result.shape == (len(SENTENCES) + 1,)

def test_task_func_case_insensitivity():
    input_string = "this is a sentence"
    result = task_func(input_string)
    expected_result = task_func("This is a sentence")
    assert np.array_equal(result, expected_result)

def test_task_func_unique_words():
    input_string = "Unique words in this sentence"
    result = task_func(input_string)
    assert isinstance(result, np.ndarray)
    assert result.shape == (len(SENTENCES) + 1,)