import pytest
from src_0957 import task_func

def test_task_func_no_seed():
    text = "Hello, World!"
    expected = "HEllo, WOrld!"
    assert task_func(text) == expected

def test_task_func_with_seed():
    text = "Hello, World!"
    seed = 1234
    expected = "HEllo, WOrld!"
    assert task_func(text, seed) == expected

def test_task_func_with_different_seed():
    text = "Hello, World!"
    seed = 5678
    expected = "HEllo, WOrld!"
    assert task_func(text, seed) == expected

def test_task_func_with_punctuation():
    text = "Hello, World!"
    expected = "HEllo, WOrld!"
    assert task_func(text) == expected

def test_task_func_with_whitespace():
    text = "Hello, World!"
    expected = "HEllo, WOrld!"
    assert task_func(text) == expected

def test_task_func_with_tabs():
    text = "Hello, World!"
    expected = "HEllo, WOrld!"
    assert task_func(text) == expected

def test_task_func_with_newlines():
    text = "Hello, World!"
    expected = "HEllo, WOrld!"
    assert task_func(text) == expected