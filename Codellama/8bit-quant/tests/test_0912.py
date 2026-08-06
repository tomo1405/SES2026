import pytest
from src_0912 import task_func

def test_task_func():
    letters = ['A', 'B', 'C']
    expected_product = 6
    assert task_func(letters) == expected_product

def test_task_func_with_empty_list():
    letters = []
    expected_product = 1
    assert task_func(letters) == expected_product

def test_task_func_with_single_letter():
    letters = ['A']
    expected_product = 1
    assert task_func(letters) == expected_product

def test_task_func_with_duplicate_letters():
    letters = ['A', 'B', 'C', 'A']
    expected_product = 6
    assert task_func(letters) == expected_product

def test_task_func_with_invalid_letters():
    letters = ['A', 'B', 'C', 'D']
    expected_product = 0
    assert task_func(letters) == expected_product