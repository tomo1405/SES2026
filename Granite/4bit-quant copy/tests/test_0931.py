import pytest
from src_0931 import task_func
import random
import string
POSSIBLE_LETTERS = ['a', 'b', 'c']

def test_task_func():
    word = "test"
    expected_output = ['tt', 'st', 'es']
    random.seed(42)  # Set the random seed for reproducibility
    actual_output = task_func(word)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_invalid_input():
    word = "123"
    with pytest.raises(ValueError) as excinfo:
        task_func(word)
    assert "Input must only contain letters." in str(excinfo.value)

def test_task_func_empty_input():
    word = ""
    expected_output = ['' for _ in range(len(POSSIBLE_LETTERS))]
    actual_output = task_func(word)
    assert actual_output == expected_output, "Output does not match expected output"