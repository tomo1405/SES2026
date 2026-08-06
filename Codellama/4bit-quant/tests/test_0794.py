import numpy as np
from src_0794 import task_func


def test_task_func():
    # Test case 1: Test with default argument
    expected = np.array(['D', 'E', 'F', 'G', 'H', 'I', 'J', 'A', 'B', 'C'])
    actual = task_func()
    assert np.array_equal(actual, expected)

    # Test case 2: Test with custom argument
    expected = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
    actual = task_func(l=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
    assert np.array_equal(actual, expected)

    # Test case 3: Test with custom argument and different length
    expected = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
    actual = task_func(l=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
    assert np.array_equal(actual, expected)

    # Test case 4: Test with custom argument and different length
    expected = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
    actual = task_func(l=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'])
    assert np.array_equal(actual, expected)

    # Test case 5: Test with custom argument and different length
    expected = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
    actual = task_func(l=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'])
    assert np.array_equal(actual, expected)