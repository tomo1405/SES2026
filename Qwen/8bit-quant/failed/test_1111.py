import pytest
from src_1111 import task_func

def test_task_func_with_empty_dict():
    assert task_func({}) == {}

def test_task_func_with_single_word():
    assert task_func({'hello': 1}) == {'l': 2, 'h': 1, 'e': 1, 'o': 1}

def test_task_func_with_multiple_words():
    assert task_func({'hello': 1, 'world': 1}) == {'l': 3, 'o': 2, 'h': 1, 'e': 1, 'w': 1, 'r': 1, 'd': 1}

def test_task_func_with_duplicate_letters():
    assert task_func({'a': 1, 'aa': 1}) == {'a': 3}

def test_task_func_with_special_characters():
    assert task_func({'hello!': 1, 'world@': 1}) == {'l': 3, 'o': 2, 'h': 1, 'e': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1, '@': 1}

def test_task_func_with_numbers_in_keys():
    assert task_func({'123': 1, '456': 1}) == {'1': 2, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1}

def test_task_func_with_case_sensitive_keys():
    assert task_func({'Hello': 1, 'hello': 1}) == {'l': 3, 'H': 1, 'e': 1, 'o': 1, 'h': 1}