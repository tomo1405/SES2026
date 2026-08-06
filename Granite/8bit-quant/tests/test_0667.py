import pytest
from src_0667 import task_func

def test_task_func():
    seq = 'abcdef'
    letter_weight_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
    expected_output = 'abcdef'
    actual_output = task_func(seq, letter_weight_dict)
    assert actual_output == expected_output

def test_task_func_with_empty_seq():
    seq = ''
    letter_weight_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
    expected_output = ''
    actual_output = task_func(seq, letter_weight_dict)
    assert actual_output == expected_output

def test_task_func_with_one_letter_seq():
    seq = 'a'
    letter_weight_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
    expected_output = 'a'
    actual_output = task_func(seq, letter_weight_dict)
    assert actual_output == expected_output

def test_task_func_with_two_letters_seq():
    seq = 'ab'
    letter_weight_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
    expected_output = 'ab'
    actual_output = task_func(seq, letter_weight_dict)
    assert actual_output == expected_output

def test_task_func_with_three_letters_seq():
    seq = 'abc'
    letter_weight_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
    expected_output = 'abc'
    actual_output = task_func(seq, letter_weight_dict)
    assert actual_output == expected_output