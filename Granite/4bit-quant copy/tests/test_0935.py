import pytest
from src_0935 import task_func

def test_task_func():
    word = "hello"
    expected_result = "b552f07f27e2e92c69c2279e080d4f3c"
    result = task_func(word)
    assert result == expected_result, "The function returned an incorrect result"

def test_task_func_with_empty_string():
    word = ""
    expected_result = "d41d8cd98f00b204e9800998ecf8427e"
    result = task_func(word)
    assert result == expected_result, "The function returned an incorrect result for an empty string"

def test_task_func_with_single_character():
    word = "a"
    expected_result = "a1606b490935679535e53156b336022c"
    result = task_func(word)
    assert result == expected_result, "The function returned an incorrect result for a single character string"