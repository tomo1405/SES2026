import pytest
from src_0836 import task_func

def test_task_func():
    # Test 1: Test with default arguments
    expected_output = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15]})
    output = task_func(n_rows=3, remove_cols=[0, 2])
    pd.testing.assert_frame_equal(output, expected_output)

    # Test 2: Test with custom arguments
    expected_output = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15]})
    output = task_func(n_rows=3, remove_cols=[0, 2], columns=['A', 'B', 'C', 'D', 'E'], random_seed=42)
    pd.testing.assert_frame_equal(output, expected_output)

    # Test 3: Test with invalid arguments
    with pytest.raises(ValueError):
        task_func(n_rows=0, remove_cols=[0, 2])

    with pytest.raises(ValueError):
        task_func(n_rows=3, remove_cols=[0, 2], columns=['A', 'B', 'C', 'D', 'E', 'F'])