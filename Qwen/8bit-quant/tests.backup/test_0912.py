import pytest
from src_0912 import task_func

def test_task_func_single_letter():
    assert task_func('A') == 1

def test_task_func_multiple_letters():
    assert task_func('ABC') == 6  # 1 * 2 * 3

def test_task_func_empty_string():
    assert task_func('') == 1

def test_task_func_single_letter_lowercase():
    with pytest.raises(KeyError):
        task_func('a')

def test_task_func_special_characters():
    with pytest.raises(KeyError):
        task_func('!@#')

def test_task_func_large_input():
    assert task_func('Z') == 26
    assert task_func('YZ') == 650  # 25 * 26

def test_task_func_repeated_letters():
    assert task_func('AAA') == 1  # 1 * 1 * 1

def test_task_func_mixed_case():
    with pytest.raises(KeyError):
        task_func('AbC')