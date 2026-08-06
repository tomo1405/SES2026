import pytest
from src_0695 import task_func

def test_task_func():
    t = [1, 2, 3, 4, 5]
    n = 3
    combinations = list(itertools.combinations(t, n))
    selected_combination = random.choice(combinations)

    assert task_func(t, n) in combinations