import pytest
from src_0667 import task_func

def test_task_func_with_positive_weights():
    seq = "abc"
    letter_weight_dict = {'a': 1, 'b': 2, 'c': 3}
    assert task_func(seq, letter_weight_dict) == "abc"

def test_task_func_with_negative_weights():
    seq = "abc"
    letter_weight_dict = {'a': -1, 'b': -2, 'c': -3}
    assert task_func(seq, letter_weight_dict) == ""

def test_task_func_with_mixed_weights():
    seq = "abc"
    letter_weight_dict = {'a': 1, 'b': -2, 'c': 3}
    assert task_func(seq, letter_weight_dict) == "ac"

def test_task_func_single_character():
    seq = "a"
    letter_weight_dict = {'a': 10}
    assert task_func(seq, letter_weight_dict) == "a"

def test_task_func_empty_sequence():
    seq = ""
    letter_weight_dict = {'a': 1, 'b': 2, 'c': 3}
    assert task_func(seq, letter_weight_dict) == ""

def test_task_func_all_same_weights():
    seq = "aaa"
    letter_weight_dict = {'a': 1}
    assert task_func(seq, letter_weight_dict) == "aaa"

def test_task_func_tie_breaker():
    seq = "ab"
    letter_weight_dict = {'a': 1, 'b': 1}
    # The function should return the first subsequence it finds with the max weight
    assert task_func(seq, letter_weight_dict) == "ab" or task_func(seq, letter_weight_dict) == "ba"