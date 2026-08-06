python
import random
import numpy as np
import pytest

def task_func(LETTERS):
    random_dict = {k: [random.randint(0, 100) for _ in range(random.randint(1, 10))] for k in LETTERS}
    mean_dict = {k: np.mean(v) for k, v in random_dict.items()}
    return mean_dict

def test_task_func():
    LETTERS = ['A', 'B', 'C']
    mean_dict = task_func(LETTERS)
    assert isinstance(mean_dict, dict)
    assert all(isinstance(v, float) for v in mean_dict.values())
    assert all(len(v) == 1 for v in mean_dict.values())