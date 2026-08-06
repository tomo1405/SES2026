import pytest
from src_0863 import task_func

def test_task_func():
    n = 10
    seed = 1234
    letter_dict = task_func(n, seed)
    assert len(letter_dict) == n
    for key, value in letter_dict.items():
        assert len(value) == 1
        assert value[0] == key

def test_task_func_with_different_seed():
    n = 10
    seed = 4321
    letter_dict = task_func(n, seed)
    assert len(letter_dict) == n
    for key, value in letter_dict.items():
        assert len(value) == 1
        assert value[0] == key

def test_task_func_with_different_n():
    n = 20
    seed = 1234
    letter_dict = task_func(n, seed)
    assert len(letter_dict) == n
    for key, value in letter_dict.items():
        assert len(value) == 1
        assert value[0] == key

def test_task_func_with_different_n_and_seed():
    n = 20
    seed = 4321
    letter_dict = task_func(n, seed)
    assert len(letter_dict) == n
    for key, value in letter_dict.items():
        assert len(value) == 1
        assert value[0] == key