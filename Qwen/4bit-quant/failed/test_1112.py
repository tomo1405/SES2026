import pytest
from src_1112 import task_func

def test_task_func_with_valid_animals():
    input_data = {
        'cat': 3,
        'dog': 5,
        'elephant': 2,
        'iguana': 1,
        'jaguar': 4
    }
    expected_output = {
        'a': 4,
        'e': 4,
        'l': 4,
        't': 4,
        'o': 3,
        'n': 3,
        'g': 3,
        'd': 3,
        'c': 2,
        'm': 2,
        'i': 2,
        'h': 1,
        'r': 1,
        'u': 1,
        'j': 1,
        'p': 1,
        'f': 1,
        'x': 1
    }
    assert task_func(input_data) == expected_output

def test_task_func_with_invalid_animals():
    input_data = {
        'cat': 3,
        'dog': 5,
        'lion': 2,  # Invalid animal
        'iguana': 1,
        'jaguar': 4
    }
    expected_output = {
        'a': 4,
        'e': 4,
        'l': 4,
        't': 4,
        'o': 3,
        'n': 3,
        'g': 3,
        'd': 3,
        'c': 2,
        'm': 2,
        'i': 2,
        'h': 1,
        'r': 1,
        'u': 1,
        'j': 1,
        'p': 1,
        'f': 1,
        'x': 1
    }
    assert task_func(input_data) == expected_output

def test_task_func_with_empty_input():
    input_data = {}
    expected_output = {}
    assert task_func(input_data) == expected_output

def test_task_func_with_single_valid_animal():
    input_data = {
        'cat': 3
    }
    expected_output = {
        'a': 2,
        't': 1,
        'c': 1
    }
    assert task_func(input_data) == expected_output

def test_task_func_with_all_valid_animals():
    input_data = {
        'cat': 3,
        'camel': 5,
        'cow': 2,
        'dog': 4,
        'elephant': 6,
        'fox': 1,
        'giraffe': 7,
        'hippo': 8,
        'iguana': 9,
        'jaguar': 10
    }
    expected_output = {
        'a': 20,
        'e': 16,
        'l': 15,
        't': 14,
        'o': 13,
        'n': 12,
        'g': 11,
        'd': 10,
        'c': 9,
        'm': 8,
        'i': 7,
        'h': 6,
        'r': 5,
        'u': 4,
        'j': 3,
        'p': 2,
        'f': 1,
        'x': 1
    }
    assert task_func(input_data) == expected_output