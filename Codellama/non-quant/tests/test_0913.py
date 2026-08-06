import pytest
from src_0913 import task_func

def test_task_func():
    letters = ['a', 'b', 'c']
    repetitions = 2
    expected_result = {'a': 2, 'b': 2, 'c': 2}
    assert task_func(letters, repetitions) == expected_result

def test_task_func_empty_input():
    letters = []
    repetitions = 0
    expected_result = {}
    assert task_func(letters, repetitions) == expected_result

def test_task_func_invalid_input():
    letters = ['a', 'b', 'c']
    repetitions = -1
    with pytest.raises(ValueError):
        task_func(letters, repetitions)