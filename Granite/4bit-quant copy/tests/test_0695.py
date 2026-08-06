import pytest
from src_0695 import task_func
import itertools
import random

def test_task_func():
    t = [1, 2, 3, 4, 5]
    n = 3
    combinations = list(itertools.combinations(t, n))
    expected_output = random.choice(combinations)
    actual_output = task_func(t, n)
    assert actual_output == expected_output

def test_task_func_with_invalid_input():
    with pytest.raises(ValueError):
        task_func([1, 2], 5)