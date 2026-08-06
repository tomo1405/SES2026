import pytest
from src_0825 import task_func

def test_task_func_no_text():
    assert task_func("") == (0, 0)

def test_task_func_only_punctuation():
    assert task_func("!!!@@@###") == (0, 9)

def test_task_func_only_words():
    assert task_func("hello world") == (2, 0)

def test_task_func_mixed_content():
    assert task_func("Hello, world!") == (2, 2)

def test_task_func_multiple_spaces():
    assert task_func("   Hello   world   ") == (2, 0)

def test_task_func_numbers():
    assert task_func("123 456") == (2, 0)

def test_task_func_alphanumeric():
    assert task_func("abc123 def456") == (2, 0)

def test_task_func_punctuation_with_words():
    assert task_func("Hello, world! How are you?") == (5, 6)

def test_task_func_special_characters():
    assert task_func("$%^&*()_+") == (0, 10)

def test_task_func_mixed_case():
    assert task_func("HeLLo WoRLD") == (2, 0)