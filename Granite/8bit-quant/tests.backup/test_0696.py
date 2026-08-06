import pytest
from src_0696 import task_func

@pytest.mark.parametrize("tuples_list, n_components, expected_output", [
    ([(1, 2), (3, 4)], 1, [[1.41421356], [2.82842712]]),
    ([(5, 6), (7, 8)], 2, [[-0.70710678, -0.70710678], [0.70710678, -0.70710678]]),
    ([(9, 10), (11, 12)], 1, [[5.47722558], [7.74596669]])
])
def test_task_func(tuples_list, n_components, expected_output):
    assert task_func(tuples_list, n_components) == expected_output