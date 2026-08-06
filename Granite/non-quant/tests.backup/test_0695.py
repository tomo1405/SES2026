import pytest
from src_0695 import task_func
import itertools
import random

@pytest.mark.parametrize("t, n, expected_output", [
    (["A", "B", "C"], 2, ["A", "B"]),
    (["1", "2", "3", "4"], 3, ["1", "2", "3"]),
    (["X", "Y", "Z"], 1, ["X"]),
    (["apple", "banana", "cherry"], 2, ["apple", "banana"]),
])
def test_task_func(t, n, expected_output):
    combinations = list(itertools.combinations(t, n))
    selected_combination = random.choice(combinations)
    assert selected_combination == expected_output