import pytest
from src_0947 import task_func

def test_task_func():
    # Test case 1: rows=3, cols=2, min_val=0, max_val=100, seed=0
    expected_output = np.array([[5, 8], [1, 9], [4, 2]])
    output = task_func(rows=3, cols=2, min_val=0, max_val=100, seed=0)
    assert np.array_equal(output, expected_output)

    # Test case 2: rows=2, cols=3, min_val=10, max_val=20, seed=1
    expected_output = np.array([[12, 15, 18], [11, 14, 17]])
    output = task_func(rows=2, cols=3, min_val=10, max_val=20, seed=1)
    assert np.array_equal(output, expected_output)

    # Test case 3: rows=1, cols=1, min_val=100, max_val=100, seed=0
    expected_output = np.array([[100]])
    output = task_func(rows=1, cols=1, min_val=100, max_val=100, seed=0)
    assert np.array_equal(output, expected_output)