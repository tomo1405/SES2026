python
import itertools
import random
import pytest

def task_func(t, n):
    combinations = list(itertools.combinations(t, n))
    selected_combination = random.choice(combinations)

    return selected_combination

def test_task_func():
    t = [1, 2, 3, 4, 5]
    n = 3
    expected_result = (1, 2, 3)

    result = task_func(t, n)

    assert result == expected_result