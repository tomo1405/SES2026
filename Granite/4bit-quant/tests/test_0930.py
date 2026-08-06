import numpy as np
from scipy import stats
from src_0930 import task_func

def test_task_func():
    # Test case 1: word is a non-empty string
    word = "hello"
    expected_difference = np.array([1, 1, 1, 1])
    expected_entropy = 1.8462871252125427
    difference, entropy = task_func(word)
    assert np.array_equal(difference, expected_difference)
    assert entropy == expected_entropy

    # Test case 2: word is an empty string
    word = ""
    expected_difference = np.array([])
    expected_entropy = 0.0
    difference, entropy = task_func(word)
    assert np.array_equal(difference, expected_difference)
    assert entropy == expected_entropy