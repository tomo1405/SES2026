import pytest
from src_0913 import task_func
from collections import Counter
import itertools

def test_task_func():
    letters = ['a', 'b', 'c']
    repetitions = 3
    expected_output = {'a': 3, 'b': 3, 'c': 3}
    actual_output = task_func(letters, repetitions)
    assert actual_output == expected_output

def test_task_func_with_empty_list():
    letters = []
    repetitions = 5
    expected_output = {}
    actual_output = task_func(letters, repetitions)
    assert actual_output == expected_output

def test_task_func_with_negative_repetitions():
    letters = ['x', 'y', 'z']
    repetitions = -2
    with pytest.raises(ValueError):
        task_func(letters, repetitions)