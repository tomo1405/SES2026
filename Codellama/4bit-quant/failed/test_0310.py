import pytest
from src_0310 import task_func

def test_task_func():
    # Test with empty list
    list_of_lists = []
    expected_result = []
    assert task_func(list_of_lists) == expected_result

    # Test with non-empty list
    list_of_lists = [[1, 2, 3], [4, 5, 6]]
    expected_result = [[0.5, 0.75], [0.25, 0.5]]
    assert task_func(list_of_lists) == expected_result

    # Test with random list
    list_of_lists = [[random.randint(0, 100) for _ in range(5)]]
    expected_result = [[random.randint(0, 100) for _ in range(5)]]
    assert task_func(list_of_lists) == expected_result

    # Test with different seed
    list_of_lists = [[1, 2, 3], [4, 5, 6]]
    expected_result = [[0.5, 0.75], [0.25, 0.5]]
    assert task_func(list_of_lists, seed=42) == expected_result