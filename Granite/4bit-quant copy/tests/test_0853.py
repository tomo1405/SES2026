import pytest
from src_0853 import task_func
import random
import string

# Test case 1: max_length is less than 1
def test_task_func_invalid_max_length():
    with pytest.raises(ValueError) as excinfo:
        task_func(max_length=0, n_samples=10)
    assert "max_length must be larger than or equal to 1." in str(excinfo.value)

# Test case 2: n_samples is less than 1
def test_task_func_invalid_n_samples():
    with pytest.raises(ValueError) as excinfo:
        task_func(max_length=10, n_samples=0)
    assert "n_samples must be larger than or equal to 1." in str(excinfo.value)

# Test case 3: valid input
def test_task_func_valid_input():
    max_length = 10
    n_samples = 5
    seed = 42
    random.seed(seed)
    expected_output = ['bvhzsqx', 'ytkfumz', 'abjwrgv', 'hjzmtta', 'owjzums']
    actual_output = task_func(max_length=max_length, n_samples=n_samples, seed=seed)
    assert actual_output == expected_output