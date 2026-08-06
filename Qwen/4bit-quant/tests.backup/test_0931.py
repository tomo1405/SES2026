import pytest
from src_0931 import task_func

def test_task_func_input_validation():
    with pytest.raises(ValueError):
        task_func("123")
    with pytest.raises(ValueError):
        task_func("!@#")

def test_task_func_short_word():
    result = task_func("a")
    assert result == ['', '', '']

def test_task_func_single_letter_repeated():
    result = task_func("aa")
    assert len(result) == 3
    assert all(pair == "aa" for pair in result)

def test_task_func_multiple_letters():
    result = task_func("abc")
    assert len(result) == 3
    assert all(pair in ["ab", "bc"] for pair in result)

def test_task_func_randomness():
    result1 = task_func("abc")
    result2 = task_func("abc")
    assert result1 != result2  # Check that results are different due to randomness

def test_task_func_with_uppercase():
    result = task_func("AbC")
    assert len(result) == 3
    assert all(pair in ["Ab", "bC"] for pair in result)