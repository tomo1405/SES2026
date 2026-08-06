import pytest
from src_0868 import task_func

def test_task_func_no_punctuation():
    text1 = "Hello, world!"
    text2 = "Python's syntax is clean."
    expected = ("Hello world", "Pythons syntax is clean")
    assert task_func(text1, text2) == expected

def test_task_func_empty_strings():
    text1 = ""
    text2 = ""
    expected = ("", "")
    assert task_func(text1, text2) == expected

def test_task_func_no_change_needed():
    text1 = "NoPunctuationHere"
    text2 = "NeitherIsHere"
    expected = ("NoPunctuationHere", "NeitherIsHere")
    assert task_func(text1, text2) == expected

def test_task_func_only_punctuation():
    text1 = "!@#$%^&*()"
    text2 = ".,;:'\"|\\/?"
    expected = ("", "")
    assert task_func(text1, text2) == expected

def test_task_func_mixed_content():
    text1 = "Mix3d C0nt3nt, with punc-tuation!"
    text2 = "An0ther example: more, punctuation?"
    expected = ("Mix3d C0nt3nt with punctuati", "An0ther example more punctuation")
    assert task_func(text1, text2) == expected