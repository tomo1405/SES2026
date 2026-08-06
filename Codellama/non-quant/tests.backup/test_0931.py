import pytest
from src_0931 import task_func

def test_task_func_valid_input():
    word = 'abc'
    expected_output = ['ab', 'bc']
    assert task_func(word) == expected_output

def test_task_func_invalid_input():
    word = '123'
    with pytest.raises(ValueError):
        task_func(word)

def test_task_func_empty_input():
    word = ''
    expected_output = ['']
    assert task_func(word) == expected_output

def test_task_func_short_input():
    word = 'ab'
    expected_output = ['ab', '']
    assert task_func(word) == expected_output