import pytest
from src_0957 import task_func

def test_task_func_with_seed():
    text = "Hello, World!"
    seed = 1234
    expected = "HElLo, WoRlD!"
    assert task_func(text, seed) == expected

def test_task_func_without_seed():
    text = "Hello, World!"
    expected = "HElLo, WoRlD!"
    assert task_func(text) == expected

def test_task_func_with_empty_string():
    text = ""
    expected = ""
    assert task_func(text) == expected

def test_task_func_with_punctuation():
    text = "Hello, World! How are you?"
    expected = "HElLo, WoRlD! HoW aRe yOu?"
    assert task_func(text) == expected

def test_task_func_with_whitespace():
    text = "Hello, World!\nHow are you?"
    expected = "HElLo, WoRlD!___HoW aRe yOu?"
    assert task_func(text) == expected

def test_task_func_with_tabs():
    text = "Hello, World!\tHow are you?"
    expected = "HElLo, WoRlD!__HoW aRe yOu?"
    assert task_func(text) == expected

def test_task_func_with_special_characters():
    text = "Hello, World! How are you?\n\t"
    expected = "HElLo, WoRlD! HoW aRe yOu?___"
    assert task_func(text) == expected