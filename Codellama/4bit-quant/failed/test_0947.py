import pytest
from src_0947 import task_func
import numpy as np
import pandas as pd

def test_task_func():
    # Test case 1: rows=3, cols=2, min_val=0, max_val=100, seed=0
    expected_output = pd.DataFrame([[0, 0], [0, 0], [0, 0]])
    actual_output = task_func(rows=3, cols=2, min_val=0, max_val=100, seed=0)
    assert np.array_equal(actual_output, expected_output)

    # Test case 2: rows=3, cols=2, min_val=0, max_val=100, seed=1
    expected_output = pd.DataFrame([[0, 0], [0, 0], [0, 0]])
    actual_output = task_func(rows=3, cols=2, min_val=0, max_val=100, seed=1)
    assert np.array_equal(actual_output, expected_output)

    # Test case 3: rows=3, cols=2, min_val=0, max_val=100, seed=2
    expected_output = pd.DataFrame([[0, 0], [0, 0], [0, 0]])
    actual_output = task_func(rows=3, cols=2, min_val=0, max_val=100, seed=2)
    assert np.array_equal(actual_output, expected_output)

    # Test case 4: rows=3, cols=2, min_val=0, max_val=100, seed=3
    expected_output = pd.DataFrame([[0, 0], [0, 0], [0, 0]])
    actual_output = task_func(rows=3, cols=2, min_val=0, max_val=100, seed=3)
    assert np.array_equal(actual_output, expected_output)

    # Test case 5: rows=3, cols=2, min_val=0, max_val=100, seed=4
    expected_output = pd.DataFrame([[0, 0], [0, 0], [0, 0]])
    actual_output = task_func(rows=3, cols=2, min_val=0, max_val=100, seed=4)
    assert np.array_equal(actual_output, expected_output)

    # Test case 6: rows=3, cols=2, min_val=0, max_val=100, seed=5
    expected_output = pd.DataFrame([[0, 0], [0, 0], [0, 0]])
    actual_output = task_func(rows=3, cols=2, min_val=0, max_val=100, seed=5)
    assert np.array_equal(actual_output, expected_output)

    # Test case 7: rows=3, cols=2, min_val=0, max_val=100, seed=6
    expected_output = pd.DataFrame([[0, 0], [0, 0], [0, 0]])
    actual_output = task_func(rows=3, cols=2, min_val=0, max_val=100, seed=6)
    assert np.array_equal(actual_output, expected_output)

    # Test case 8: rows=3, cols=2, min_val=0, max_val=100, seed=7
    expected_output = pd.DataFrame([[0, 0], [0, 0], [0, 0]])
    actual_output = task_func(rows=3, cols=2, min_val=0, max_val=100, seed=7)
    assert np.array_equal(actual_output, expected_output)

    # Test case 9: rows=3, cols=2, min_val=0, max_val=100, seed=8
    expected_output = pd.DataFrame([[0, 0], [0, 0], [0, 0]])
    actual_output = task_func(rows=3, cols=2, min_val=0, max_val=100, seed=8)
    assert np.array_equal(actual_output, expected_output)

    # Test case 10: rows=3, cols=2, min_val=0, max_val=100, seed=9
    expected_output = pd.DataFrame([[0, 0], [0, 0], [0, 0]])
    actual_output = task_func(rows=3, cols=2, min_val=0, max_val=100, seed=9)
    assert np.array_equal(actual_output, expected_output)