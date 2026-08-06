import pytest
from src_1112 import task_func

def test_task_func_empty_input():
    assert task_func({}) == {}

def test_task_func_no_matching_animals():
    input_dict = {'lion': 1, 'tiger': 2, 'bear': 3}
    assert task_func(input_dict) == {}

def test_task_func_single_matching_animal():
    input_dict = {'cat': 1}
    assert task_func(input_dict) == {'c': 1, 'a': 1, 't': 1}

def test_task_func_multiple_matching_animals():
    input_dict = {'cat': 1, 'dog': 2, 'elephant': 3}
    expected_output = {'e': 3, 'l': 3, 'n': 3, 'a': 3, 't': 3, 'o': 2, 'd': 2, 'g': 2, 'c': 1}
    assert task_func(input_dict) == expected_output

def test_task_func_duplicate_letters():
    input_dict = {'cat': 2, 'dog': 2}
    expected_output = {'t': 4, 'a': 2, 'c': 2, 'o': 2, 'd': 2, 'g': 2}
    assert task_func(input_dict) == expected_output

def test_task_func_case_insensitivity():
    input_dict = {'CAT': 1, 'DOG': 2, 'ELEPHANT': 3}
    expected_output = {'e': 3, 'l': 3, 'n': 3, 'a': 3, 't': 3, 'o': 2, 'd': 2, 'g': 2, 'c': 1}
    assert task_func(input_dict) == expected_output

def test_task_func_non_string_keys():
    input_dict = {1: 'cat', 2: 'dog'}
    assert task_func(input_dict) == {}