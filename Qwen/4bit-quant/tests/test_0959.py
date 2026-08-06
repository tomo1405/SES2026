import pytest
from src_0959 import task_func

def test_task_func_no_seed():
    text = "hello world"
    result = task_func(text)
    assert result != text, "The scrambled text should be different from the original"

def test_task_func_with_seed():
    text = "hello world"
    seed = 42
    result = task_func(text, seed=seed)
    expected_result = "hlelo wrold"  # Known scrambled result with seed 42
    assert result == expected_result, f"Expected '{expected_result}', but got '{result}'"

def test_task_func_short_words():
    text = "a bc de"
    result = task_func(text)
    assert result == text, "Short words should remain unchanged"

def test_task_func_empty_string():
    text = ""
    result = task_func(text)
    assert result == text, "Empty string should remain unchanged"

def test_task_func_punctuation():
    text = "hello, world!"
    result = task_func(text)
    assert result == "hlelo, wrold!", "Punctuation should remain in place"

def test_task_func_numbers():
    text = "hello123 world456"
    result = task_func(text)
    assert result == "hlelo123 wrold456", "Numbers should remain in place"