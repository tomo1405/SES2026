import pytest
from src_0935 import task_func

def test_task_func():
    word = "hello"
    expected_result = "b5d89c5002b7f0796d728e2d2b360578"
    result = task_func(word)
    assert result == expected_result, "The function returned an incorrect result"

def test_task_func_with_empty_string():
    word = ""
    expected_result = "d41d8cd98f00b204e9800998ecf8427e"
    result = task_func(word)
    assert result == expected_result, "The function returned an incorrect result"

def test_task_func_with_single_character():
    word = "a"
    expected_result = "a51d9946d2f0408ba5c0521b06062c6d"
    result = task_func(word)
    assert result == expected_result, "The function returned an incorrect result"