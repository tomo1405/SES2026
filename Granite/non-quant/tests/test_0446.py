import numpy as np
import pytest
from src_0446 import task_func


@pytest.mark.parametrize("points, seed, expected_output", [
    (np.array([[0, 0], [1, 1], [2, 2]]), 0, (vor, ax)),
    (np.array([[0, 0], [1, 1], [2, 2], [3, 3]]), 0, (vor, ax)),
    (np.array([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]), 0, (vor, ax)),
    (np.array([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]), 0, (vor, ax)),
    (np.array([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]), 0, (vor, ax)),
    (np.array([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]), 0, (vor, ax)),
    (np.array([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]), 0, (vor, ax)),
    (np.array([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]), 0, (vor, ax)),
    (np.array([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]), 0, (vor, ax)),
])
def test_task_func(points, seed, expected_output):
    vor, ax = task_func(points, seed)
    assert (vor, ax) == expected_output