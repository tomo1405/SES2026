import numpy as np
from src_0794 import task_func


def test_task_func():
    # Test case 1: l is None
    l = None
    expected = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
    np.testing.assert_array_equal(task_func(l), expected)

    # Test case 2: l is a list
    l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    expected = np.array(['D', 'E', 'F', 'G', 'H', 'I', 'A', 'B', 'C'])
    np.testing.assert_array_equal(task_func(l), expected)

    # Test case 3: l is a numpy array
    l = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
    expected = np.array(['D', 'E', 'F', 'G', 'H', 'I', 'A', 'B', 'C'])
    np.testing.assert_array_equal(task_func(l), expected)

    # Test case 4: l is a list with duplicates
    l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'A']
    expected = np.array(['D', 'E', 'F', 'G', 'H', 'I', 'A', 'B', 'C'])
    np.testing.assert_array_equal(task_func(l), expected)

    # Test case 5: l is a numpy array with duplicates
    l = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'A'])
    expected = np.array(['D', 'E', 'F', 'G', 'H', 'I', 'A', 'B', 'C'])
    np.testing.assert_array_equal(task_func(l), expected)