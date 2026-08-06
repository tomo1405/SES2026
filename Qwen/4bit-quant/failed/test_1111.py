import pytest
from src_1111 import task_func

def test_task_func_with_empty_dict():
    assert task_func({}) == {}

def test_task_func_with_single_word():
    assert task_func({'hello': 1}) == {'l': 2, 'h': 1, 'e': 1, 'o': 1}

def test_task_func_with_multiple_words():
    assert task_func({'hello': 1, 'world': 1}) == {'l': 3, 'o': 2, 'h': 1, 'w': 1, 'r': 1, 'd': 1}

def test_task_func_with_repeated_letters():
    assert task_func({'aabbcc': 1}) == {'a': 2, 'b': 2, 'c': 2}

def test_task_func_with_different_cases():
    assert task_func({'Hello': 1, 'World': 1}) == {'l': 3, 'o': 2, 'H': 1, 'W': 1, 'r': 1, 'd': 1}

def test_task_func_with_numbers_in_keys():
    assert task_func({'abc123': 1}) == {'a': 1, 'b': 1, 'c': 1, '1': 1, '2': 1, '3': 1}

def test_task_func_with_special_characters():
    assert task_func({'!@#': 1}) == {'!': 1, '@': 1, '#': 1}