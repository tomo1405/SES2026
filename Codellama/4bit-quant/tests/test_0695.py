import itertools
import random

import pytest
from src_0695 import task_func


def test_task_func():
    t = [1, 2, 3, 4, 5]
    n = 3
    combinations = list(itertools.combinations(t, n))
    selected_combination = random.choice(combinations)

    assert selected_combination in combinations

def test_task_func_invalid_input():
    t = [1, 2, 3, 4, 5]
    n = 6
    with pytest.raises(ValueError):
        task_func(t, n)