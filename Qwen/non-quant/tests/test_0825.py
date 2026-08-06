import pytest
from src_0825 import task_func

def test_task_func_no_text():
    assert task_func("") == (0, 0)

def test_task_func_no_punctuation():
    assert task_func("Hello World") == (2, 0)

def test_task_func_only_punctuation():
    assert task_func("!@#$%^&*()") == (0, 10)

def test_task_func_mixed_text():
    assert task_func("Hello, World!") == (2, 2)

def test_task_func_with_numbers():
    assert task_func("Hello123, World456!") == (2, 2)

def test_task_func_with_special_characters():
    assert task_func("Hello_World!@#") == (2, 3)

def test_task_func_long_text():
    assert task_func("This is a long sentence with multiple words and punctuation!!!") == (11, 3)