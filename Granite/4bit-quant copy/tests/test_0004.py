import pytest
from src_0004 import task_func

def test_task_func():
    # Test case 1: Test with an empty input
    result = task_func([])
    expected_result = {}
    assert result == expected_result

    # Test case 2: Test with a non-empty input
    result = task_func(['A', 'B', 'C'])
    expected_result = {'A': 50.0, 'B': 50.0, 'C': 50.0}
    assert result == expected_result

    # Test case 3: Test with a non-empty input and a custom seed
    random.seed(42)
    np.random.seed(42)
    result = task_func(['X', 'Y', 'Z'])
    expected_result = {'X': 50.0, 'Y': 50.0, 'Z': 50.0}
    assert result == expected_result