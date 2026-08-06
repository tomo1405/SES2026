import pytest
from src_0930 import task_func

def test_task_func_empty_string():
    assert task_func("") == (np.array([]), 0)

def test_task_func_single_char():
    assert task_func("a") == (np.array([0]), 0)

def test_task_func_two_chars():
    assert task_func("ab") == (np.array([-1]), 0)

def test_task_func_three_chars():
    assert task_func("abc") == (np.array([-1, -1]), 0)

def test_task_func_four_chars():
    assert task_func("abcd") == (np.array([-1, -1, -1]), 0)

def test_task_func_five_chars():
    assert task_func("abcde") == (np.array([-1, -1, -1, -1]), 0)

def test_task_func_six_chars():
    assert task_func("abcdef") == (np.array([-1, -1, -1, -1, -1]), 0)

def test_task_func_seven_chars():
    assert task_func("abcdefg") == (np.array([-1, -1, -1, -1, -1, -1]), 0)

def test_task_func_eight_chars():
    assert task_func("abcdefgh") == (np.array([-1, -1, -1, -1, -1, -1, -1]), 0)

def test_task_func_nine_chars():
    assert task_func("abcdefghi") == (np.array([-1, -1, -1, -1, -1, -1, -1, -1]), 0)

def test_task_func_ten_chars():
    assert task_func("abcdefghij") == (np.array([-1, -1, -1, -1, -1, -1, -1, -1, -1]), 0)