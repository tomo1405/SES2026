import pytest
from src_0959 import task_func

def test_task_func_no_seed():
    text = "hello world"
    result = task_func(text)
    # Since no seed is provided, we can't predict the exact output,
    # but we can check if the words are scrambled correctly.
    assert result != text
    words = result.split()
    assert len(words) == 2
    assert words[0][0] == 'h' and words[0][-1] == 'o'
    assert words[1][0] == 'w' and words[1][-1] == 'd'

def test_task_func_with_seed():
    text = "hello world"
    seed = 42
    result = task_func(text, seed=seed)
    expected_result = "ehllo wlord"
    assert result == expected_result

def test_task_func_single_word():
    text = "hi"
    result = task_func(text)
    assert result == text  # Single word shorter than 4 characters should remain unchanged

def test_task_func_empty_string():
    text = ""
    result = task_func(text)
    assert result == text  # Empty string should remain unchanged

def test_task_func_punctuation():
    text = "hello, world!"
    result = task_func(text)
    assert result == "ehllo, wlord!"  # Punctuation should remain in place

def test_task_func_numbers():
    text = "abc123"
    result = task_func(text)
    assert result == "bac123"  # Numbers should be included in the scrambling

def test_task_func_multiple_words():
    text = "this is a test"
    seed = 42
    result = task_func(text, seed=seed)
    expected_result = "hist si a estt"
    assert result == expected_result