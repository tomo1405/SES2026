import math

import pytest
from src_0855 import task_func


def test_task_func():
    with pytest.raises(TypeError):
        task_func("not a list")

    with pytest.raises(TypeError):
        task_func([1, 2, "not an integer"])

    with pytest.raises(ValueError):
        task_func([-1, 2, 3])

    assert task_func([]) == ([], [])

    result = task_func([1, 2, 3])
    expected_sums = [math.factorial(1) + math.factorial(2) + math.factorial(3),
                     math.factorial(1) + math.factorial(2) + math.factorial(1),
                     math.factorial(1) + math.factorial(3) + math.factorial(2),
                     math.factorial(2) + math.factorial(1) + math.factorial(3),
                     math.factorial(2) + math.factorial(3) + math.factorial(1),
                     math.factorial(3) + math.factorial(1) + math.factorial(2)]
    expected_permutations = [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
    assert result[0] == expected_sums
    assert result[1] == expected_permutations