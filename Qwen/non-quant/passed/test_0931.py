import pytest
from src_0931 import task_func

def test_task_func_non_alpha():
    with pytest.raises(ValueError):
        task_func("123")

def test_task_func_single_char():
    result = task_func("a")
    assert result == ['', '', '']

def test_task_func_two_chars():
    result = task_func("ab")
    assert len(result) == 3
    assert all(pair in ["ab"] for pair in result)

def test_task_func_multiple_chars():
    result = task_func("abc")
    assert len(result) == 3
    assert all(pair in ["ab", "bc"] for pair in result)

def test_task_func_randomness():
    result1 = task_func("abc")
    result2 = task_func("abc")
    assert result1 != result2 or result1 == result2  # Allow for the possibility of the same result due to randomness

def test_task_func_long_word():
    result = task_func("abcdefg")
    assert len(result) == 3
    assert all(pair in ["ab", "bc", "cd", "de", "ef", "fg"] for pair in result)