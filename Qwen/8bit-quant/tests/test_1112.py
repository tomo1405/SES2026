import pytest
from src_1112 import task_func

def test_task_func_empty_input():
    assert task_func({}) == {}

def test_task_func_no_matching_animals():
    input_dict = {'zebra': 1, 'kangaroo': 2}
    assert task_func(input_dict) == {}

def test_task_func_single_animal():
    input_dict = {'cat': 3}
    expected_output = {'c': 1, 'a': 1, 't': 1}
    assert task_func(input_dict) == expected_output

def test_task_func_multiple_animals():
    input_dict = {'cat': 3, 'dog': 2, 'elephant': 1}
    expected_output = {'e': 2, 'l': 2, 'a': 2, 'n': 2, 't': 2, 'd': 1, 'o': 1, 'g': 1, 'c': 1}
    assert task_func(input_dict) == expected_output

def test_task_func_case_insensitivity():
    input_dict = {'CAT': 3, 'DOG': 2, 'ELEPHANT': 1}
    expected_output = {'e': 2, 'l': 2, 'a': 2, 'n': 2, 't': 2, 'd': 1, 'o': 1, 'g': 1, 'c': 1}
    assert task_func(input_dict) == expected_output

def test_task_func_non_string_keys():
    input_dict = {1: 3, 2: 2, 'elephant': 1}
    expected_output = {'e': 2, 'l': 2, 'a': 2, 'n': 2, 't': 2}
    assert task_func(input_dict) == expected_output

def test_task_func_with_numbers_in_values():
    input_dict = {'cat': 3, 'dog': 2, 'elephant': 1, 'iguana': 4}
    expected_output = {'e': 3, 'l': 3, 'a': 2, 'n': 2, 't': 2, 'i': 1, 'g': 1, 'u': 1, 'c': 1, 'd': 1, 'o': 1}
    assert task_func(input_dict) == expected_output

def test_task_func_with_special_characters():
    input_dict = {'cat!': 3, 'dog@': 2, 'elephant#': 1}
    expected_output = {'e': 2, 'l': 2, 'a': 2, 'n': 2, 't': 2, 'd': 1, 'o': 1, 'g': 1, 'c': 1}
    assert task_func(input_dict) == expected_output