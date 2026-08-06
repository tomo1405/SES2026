import pytest
from src_0853 import task_func

def test_task_func_positive():
    # Test with valid input
    max_length = 5
    n_samples = 10
    seed = 1234
    expected_output = [
        'abcde',
        'abcd',
        'abc',
        'ab',
        'a',
        'bcde',
        'bcd',
        'bc',
        'b',
        'cde'
    ]
    assert task_func(max_length, n_samples, seed) == expected_output

def test_task_func_negative():
    # Test with invalid input
    max_length = 0
    n_samples = 10
    seed = 1234
    with pytest.raises(ValueError):
        task_func(max_length, n_samples, seed)