import pytest
from src_0912 import task_func

def test_task_func_single_letter():
    assert task_func(['A']) == 1
    assert task_func(['Z']) == 26

def test_task_func_multiple_letters():
    assert task_func(['A', 'B', 'C']) == 6  # 1 * 2 * 3
    assert task_func(['X', 'Y', 'Z']) == 702  # 24 * 25 * 26

def test_task_func_mixed_case():
    assert task_func(['a', 'B', 'c']) == 6  # 1 * 2 * 3 (case should be ignored)
    assert task_func(['Z', 'y', 'x']) == 702  # 26 * 25 * 24 (case should be ignored)

def test_task_func_empty_list():
    assert task_func([]) == 1  # No letters, product should be 1

def test_task_func_single_letter_repeated():
    assert task_func(['A', 'A', 'A']) == 1  # 1 * 1 * 1
    assert task_func(['Z', 'Z', 'Z']) == 17576  # 26 * 26 * 26

def test_task_func_large_input():
    assert task_func(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')) == 10888869450418352160768000000  # Product of numbers 1 to 26