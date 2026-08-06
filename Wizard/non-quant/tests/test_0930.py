python
import numpy as np
import scipy.stats as stats

def test_task_func():
    # Test case 1: normal input
    word = "hello"
    expected_difference = np.array([104, 101, 108, 108, 111])
    expected_entropy = 2.302585092994046
    actual_difference, actual_entropy = task_func(word)
    assert np.array_equal(expected_difference, actual_difference)
    assert np.isclose(expected_entropy, actual_entropy)

    # Test case 2: empty string input
    word = ""
    expected_difference = np.array([])
    expected_entropy = 0.0
    actual_difference, actual_entropy = task_func(word)
    assert np.array_equal(expected_difference, actual_difference)
    assert np.isclose(expected_entropy, actual_entropy)

    # Test case 3: input with only one character
    word = "a"
    expected_difference = np.array([97])
    expected_entropy = 0.0
    actual_difference, actual_entropy = task_func(word)
    assert np.array_equal(expected_difference, actual_difference)
    assert np.isclose(expected_entropy, actual_entropy)