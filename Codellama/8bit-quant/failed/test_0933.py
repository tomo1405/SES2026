import pytest
from src_0933 import task_func

def test_task_func_empty_string():
    assert task_func("") == []

def test_task_func_single_letter():
    assert task_func("a") == []

def test_task_func_two_letters():
    assert task_func("ab") == [("ab", 1)]

def test_task_func_three_letters():
    assert task_func("abc") == [("ab", 1), ("bc", 1)]

def test_task_func_four_letters():
    assert task_func("abcd") == [("ab", 1), ("bc", 1), ("cd", 1)]

def test_task_func_five_letters():
    assert task_func("abcde") == [("ab", 1), ("bc", 1), ("cd", 1), ("de", 1)]

def test_task_func_six_letters():
    assert task_func("abcdef") == [("ab", 1), ("bc", 1), ("cd", 1), ("de", 1), ("ef", 1)]

def test_task_func_seven_letters():
    assert task_func("abcdefg") == [("ab", 1), ("bc", 1), ("cd", 1), ("de", 1), ("ef", 1), ("fg", 1)]

def test_task_func_eight_letters():
    assert task_func("abcdefgh") == [("ab", 1), ("bc", 1), ("cd", 1), ("de", 1), ("ef", 1), ("fg", 1), ("gh", 1)]

def test_task_func_nine_letters():
    assert task_func("abcdefghi") == [("ab", 1), ("bc", 1), ("cd", 1), ("de", 1), ("ef", 1), ("fg", 1), ("gh", 1), ("hi", 1)]

def test_task_func_ten_letters():
    assert task_func("abcdefghij") == [("ab", 1), ("bc", 1), ("cd", 1), ("de", 1), ("ef", 1), ("fg", 1), ("gh", 1), ("hi", 1), ("ij", 1)]