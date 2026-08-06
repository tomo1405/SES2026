import pytest
from src_0741 import task_func
from collections import Counter
import heapq

def test_task_func_with_unique_letters():
    my_dict = {'a': 5, 'b': 3, 'c': 8, 'd': 2}
    expected_output = ['c', 'a', 'b']
    assert task_func(my_dict) == expected_output

def test_task_func_with_tie():
    my_dict = {'a': 5, 'b': 5, 'c': 8, 'd': 2}
    expected_output = ['c', 'a', 'b']
    assert task_func(my_dict) == expected_output

def test_task_func_with_less_than_three_letters():
    my_dict = {'a': 5, 'b': 3}
    expected_output = ['a', 'b']
    assert task_func(my_dict) == expected_output

def test_task_func_with_empty_dict():
    my_dict = {}
    expected_output = []
    assert task_func(my_dict) == expected_output

def test_task_func_with_all_same_frequency():
    my_dict = {'a': 1, 'b': 1, 'c': 1}
    expected_output = ['a', 'b', 'c']
    assert task_func(my_dict) == expected_output

def test_task_func_with_non_alphabetical_keys():
    my_dict = {'1': 5, '2': 3, '3': 8, '4': 2}
    expected_output = []
    assert task_func(my_dict) == expected_output

def test_task_func_with_negative_values():
    my_dict = {'a': -5, 'b': -3, 'c': -8, 'd': -2}
    expected_output = []
    assert task_func(my_dict) == expected_output