import pytest
from src_0667 import task_func

def test_task_func():
    seq = 'abcde'
    letter_weight_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    expected_result = 'abcde'
    assert task_func(seq, letter_weight_dict) == expected_result

def test_task_func_empty_seq():
    seq = ''
    letter_weight_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    expected_result = ''
    assert task_func(seq, letter_weight_dict) == expected_result

def test_task_func_empty_weight_dict():
    seq = 'abcde'
    letter_weight_dict = {}
    expected_result = ''
    assert task_func(seq, letter_weight_dict) == expected_result

def test_task_func_invalid_weight_dict():
    seq = 'abcde'
    letter_weight_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
    expected_result = ''
    assert task_func(seq, letter_weight_dict) == expected_result

def test_task_func_invalid_seq():
    seq = 'abcde'
    letter_weight_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    expected_result = ''
    assert task_func(seq, letter_weight_dict) == expected_result