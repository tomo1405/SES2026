import pytest
from src_0276 import task_func
import numpy as np
from itertools import combinations

def test_task_func_with_valid_input():
    n = 5
    expected_output = [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
    actual_output = task_func(n)
    assert actual_output == expected_output

def test_task_func_with_invalid_input():
    n = 0
    with pytest.raises(ValueError) as excinfo:
        task_func(n)
    assert "Input must be a positive integer" in str(excinfo.value)