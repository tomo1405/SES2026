import pytest
from src_0913 import task_func

def test_task_func_single_repetition():
    letters = ['a', 'b', 'c']
    repetitions = 1
    expected_output = {'a': 1, 'b': 1, 'c': 1}
    assert task_func(letters, repetitions) == expected_output

def test_task_func_multiple_repetitions():
    letters = ['x', 'y', 'z']
    repetitions = 3
    expected_output = {'x': 3, 'y': 3, 'z': 3}
    assert task_func(letters, repetitions) == expected_output

def test_task_func_empty_list():
    letters = []
    repetitions = 5
    expected_output = {}
    assert task_func(letters, repetitions) == expected_output

def test_task_func_single_letter():
    letters = ['a']
    repetitions = 4
    expected_output = {'a': 4}
    assert task_func(letters, repetitions) == expected_output

def test_task_func_no_repetitions():
    letters = ['m', 'n', 'o']
    repetitions = 0
    expected_output = {}
    assert task_func(letters, repetitions) == expected_output

def test_task_func_with_duplicates():
    letters = ['p', 'q', 'p', 'r']
    repetitions = 2
    expected_output = {'p': 4, 'q': 2, 'r': 2}
    assert task_func(letters, repetitions) == expected_output