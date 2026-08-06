import pytest
from src_0930 import task_func
import numpy as np
from scipy import stats

def test_task_func():
    # Test case 1: word with only one character
    word = "a"
    expected_difference = np.array([0])
    expected_entropy = 0
    difference, entropy = task_func(word)
    assert np.array_equal(difference, expected_difference)
    assert entropy == expected_entropy

    # Test case 2: word with multiple characters
    word = "hello"
    expected_difference = np.array([1, 1, 1, 1])
    expected_entropy = stats.entropy(expected_difference)
    difference, entropy = task_func(word)
    assert np.array_equal(difference, expected_difference)
    assert entropy == expected_entropy

    # Test case 3: empty string
    word = ""
    expected_difference = np.array([])
    expected_entropy = 0
    difference, entropy = task_func(word)
    assert np.array_equal(difference, expected_difference)
    assert entropy == expected_entropy