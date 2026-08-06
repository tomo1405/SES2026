import pytest
from src_0958 import task_func

def test_task_func_empty_string():
    result = task_func("")
    assert result == (0, 0, 0)

def test_task_func_no_punctuation_no_spaces():
    result = task_func("abc")
    assert result == (1, 3, 3)

def test_task_func_with_punctuation():
    result = task_func("a,b!c?")
    assert result == (1, 3, 3)

def test_task_func_with_spaces():
    result = task_func("a b c")
    assert result == (3, 3, 3)

def test_task_func_with_mixed_content():
    result = task_func("Hello, world!")
    assert result == (2, 10, 7)

def test_task_func_with_repeated_chars():
    result = task_func("a a a")
    assert result == (3, 3, 1)

def test_task_func_with_special_chars():
    result = task_func("123 @#%")
    assert result == (1, 6, 6)

def test_task_func_with_newlines():
    result = task_func("a\nb\nc")
    assert result == (3, 3, 3)