import pytest
from src_0959 import task_func

def test_task_func_no_seed():
    text = "hello world"
    result = task_func(text)
    assert result != text, "The scrambled text should be different from the original text"

def test_task_func_with_seed():
    text = "hello world"
    seed = 42
    result = task_func(text, seed=seed)
    expected = "hlelo wlord"
    assert result == expected, f"Expected {expected}, but got {result}"

def test_task_func_single_word():
    text = "hi"
    result = task_func(text)
    assert result == text, "Words with 3 or fewer characters should remain unchanged"

def test_task_func_multiple_words():
    text = "this is a test"
    seed = 42
    result = task_func(text, seed=seed)
    expected = "thsi si a tset"
    assert result == expected, f"Expected {expected}, but got {result}"

def test_task_func_empty_string():
    text = ""
    result = task_func(text)
    assert result == text, "An empty string should return an empty string"

def test_task_func_punctuation():
    text = "Hello, world!"
    seed = 42
    result = task_func(text, seed=seed)
    expected = "Hlelo, wlord!"
    assert result == expected, f"Expected {expected}, but got {result}"