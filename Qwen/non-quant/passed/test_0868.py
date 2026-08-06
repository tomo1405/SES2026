import pytest
from src_0868 import task_func

def test_task_func_no_punctuation():
    text1 = "Hello, world!"
    text2 = "Python is fun."
    expected = ("Hello world", "Python is fun")
    assert task_func(text1, text2) == expected

def test_task_func_with_special_characters():
    text1 = "Hello!!!"
    text2 = "Python@#"
    expected = ("Hello", "Python")
    assert task_func(text1, text2) == expected

def test_task_func_empty_strings():
    text1 = ""
    text2 = ""
    expected = ("", "")
    assert task_func(text1, text2) == expected

def test_task_func_only_punctuation():
    text1 = "!@#$%^&*()"
    text2 = ".,;:"
    expected = ("", "")
    assert task_func(text1, text2) == expected

def test_task_func_mixed_content():
    text1 = "Hello, World! 123"
    text2 = "Python-3.8 is great."
    expected = ("Hello World 123", "Python38 is great")
    assert task_func(text1, text2) == expected