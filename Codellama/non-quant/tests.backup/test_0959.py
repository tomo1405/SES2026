import pytest
from src_0959 import task_func

def test_task_func_with_seed():
    text = "The quick brown fox jumps over the lazy dog"
    seed = 1234
    expected_output = "The qick brwn fox jmps ovver the lzy dog"
    assert task_func(text, seed) == expected_output

def test_task_func_without_seed():
    text = "The quick brown fox jumps over the lazy dog"
    expected_output = "The qick brwn fox jmps ovver the lzy dog"
    assert task_func(text) == expected_output

def test_task_func_with_empty_string():
    text = ""
    expected_output = ""
    assert task_func(text) == expected_output

def test_task_func_with_single_word():
    text = "The"
    expected_output = "The"
    assert task_func(text) == expected_output

def test_task_func_with_multiple_words():
    text = "The quick brown fox jumps over the lazy dog"
    expected_output = "The qick brwn fox jmps ovver the lzy dog"
    assert task_func(text) == expected_output

def test_task_func_with_special_characters():
    text = "The quick brown fox jumps over the lazy dog!"
    expected_output = "The qick brwn fox jmps ovver the lzy dog!"
    assert task_func(text) == expected_output

def test_task_func_with_unicode_characters():
    text = "The quick brown fox jumps over the lazy dog 🐕"
    expected_output = "The qick brwn fox jmps ovver the lzy dog 🐕"
    assert task_func(text) == expected_output