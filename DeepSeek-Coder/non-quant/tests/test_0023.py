import pytest
from src_0023 import task_func

@pytest.mark.parametrize("l1, l2, K, expected", [
    ([1, 2, 3], [4, 5, 6], 3, {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1}),
    ([], [], 5, {}),
    ([1], [2], 1, {'1': 1, '2': 1}),
    ([1, 2], [3, 4], 2, {'1': 1, '2': 1, '3': 1, '4': 1}),
])
def test_task_func(l1, l2, K, expected):
    result = task_func(l1, l2, K=K)
    assert result == expected