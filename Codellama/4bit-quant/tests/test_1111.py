import pytest
from src_1111 import task_func

def test_task_func():
    word_dict = {'hello': 1, 'world': 2, 'python': 3}
    expected_result = {'hello': 1, 'world': 2, 'python': 3}
    assert task_func(word_dict) == expected_result

def test_task_func_empty_dict():
    word_dict = {}
    expected_result = {}
    assert task_func(word_dict) == expected_result

def test_task_func_single_key():
    word_dict = {'hello': 1}
    expected_result = {'hello': 1}
    assert task_func(word_dict) == expected_result

def test_task_func_multiple_keys():
    word_dict = {'hello': 1, 'world': 2, 'python': 3}
    expected_result = {'hello': 1, 'world': 2, 'python': 3}
    assert task_func(word_dict) == expected_result

def test_task_func_duplicate_keys():
    word_dict = {'hello': 1, 'world': 2, 'python': 3, 'hello': 4}
    expected_result = {'hello': 5, 'world': 2, 'python': 3}
    assert task_func(word_dict) == expected_result