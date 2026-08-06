python
import numpy as np
import pytest
from scipy import stats
from src_0930 import task_func

def test_task_func():
    # Test case 1: normal input
    word = "hello"
    expected_difference = np.array([104, 101, 108, 108, 111])
    expected_entropy = 2.9444389791664404
    difference, entropy = task_func(word)
    assert np.array_equal(difference, expected_difference)
    assert entropy == pytest.approx(expected_entropy)

    # Test case 2: empty string input
    word = ""
    expected_difference = np.array([])
    expected_entropy = 0.0
    difference, entropy = task_func(word)
    assert np.array_equal(difference, expected_difference)
    assert entropy == pytest.approx(expected_entropy)

    # Test case 3: input with only one character
    word = "a"
    expected_difference = np.array([97])
    expected_entropy = 0.0
    difference, entropy = task_func(word)
    assert np.array_equal(difference, expected_difference)
    assert entropy == pytest.approx(expected_entropy)