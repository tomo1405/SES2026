import pytest
from src_0935 import task_func

def test_task_func():
    word = "hello"
    expected_result = "b5d898b10f21f942e69b72830813a994"
    result = task_func(word)
    assert result == expected_result, "The function returned an incorrect result"

def test_task_func_with_empty_string():
    word = ""
    expected_result = "d41d8cd98f00b204e9800998ecf8427e"
    result = task_func(word)
    assert result == expected_result, "The function returned an incorrect result"

def test_task_func_with_single_character():
    word = "a"
    expected_result = "a94a8fe5ccb19ba61c4c0873d391e987"
    result = task_func(word)
    assert result == expected_result, "The function returned an incorrect result"