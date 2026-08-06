import pytest
from src_0912 import task_func

def test_task_func_single_letter():
    assert task_func('A') == 1
    assert task_func('B') == 2
    assert task_func('Z') == 26

def test_task_func_multiple_letters():
    assert task_func('AB') == 2
    assert task_func('AZ') == 52
    assert task_func('ZA') == 52

def test_task_func_empty_string():
    assert task_func('') == 1

def test_task_func_case_insensitivity():
    assert task_func('a') == 1
    assert task_func('z') == 26

def test_task_func_long_string():
    assert task_func('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 26 ** 26

def test_task_func_special_characters():
    with pytest.raises(KeyError):
        task_func('!@#')