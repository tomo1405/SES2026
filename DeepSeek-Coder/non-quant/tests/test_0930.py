import pytest
from src_0930 import task_func
import numpy as np
from scipy import stats

def test_task_func_empty_string():
    result = task_func("")
    assert result == (np.array([]), 0.0)

def test_task_func_single_character():
    result = task_func("a")
    assert result == (np.array([97]), 0.0)

def test_task_func_multiple_characters():
    result = task_func("abc")
    expected_difference = np.array([ord('b') - ord('a'), ord('c') - ord('b')])
    expected_entropy = stats.entropy([0.5, 0.5])
    assert result == (expected_difference, expected_entropy)