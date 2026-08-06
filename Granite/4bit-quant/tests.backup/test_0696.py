import pytest
from src_0696 import task_func

@pytest.mark.parametrize("tuples_list, n_components, expected_output", [
    ([[1, 2], [3, 4]], 1, [[-1.11684397], [1.11684397]]),
    ([[5, 6], [7, 8]], 2, [[-1.11684397, 0.40824829], [1.11684397, -0.40824829]]),
])
def test_task_func(tuples_list, n_components, expected_output):
    assert task_func(tuples_list, n_components) == expected_output