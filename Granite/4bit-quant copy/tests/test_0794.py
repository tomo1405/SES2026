import pytest
from src_0794 import task_func

def test_task_func():
    # Test case 1: Default input
    expected_output = np.array(['D', 'E', 'F', 'G', 'H', 'I', 'J', 'A', 'B', 'C'])
    actual_output = task_func()
    assert np.array_equal(actual_output, expected_output)

    # Test case 2: Custom input
    input_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    expected_output = np.array(['d', 'e', 'f', 'g', 'h', 'i', 'j', 'a', 'b', 'c'])
    actual_output = task_func(input_list)
    assert np.array_equal(actual_output, expected_output)

    # Test case 3: Empty input
    expected_output = np.array([])
    actual_output = task_func([])
    assert np.array_equal(actual_output, expected_output)