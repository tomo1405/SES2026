import pytest
from src_0687 import task_func

@pytest.mark.parametrize("list_of_lists, expected_output", [
    ([[1, 2, 3], [4, 5, 6]], [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]]),
    ([[1, 2], [3, 4], [5, 6]], [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 0, 0], [0, 1, 0], [0, 0, 1]]),
    ([[1], [2], [3], [4], [5], [6]], [[1], [0], [0], [0], [0], [0]]),
])
def test_task_func(list_of_lists, expected_output):
    actual_output = task_func(list_of_lists)
    assert actual_output.tolist() == expected_output