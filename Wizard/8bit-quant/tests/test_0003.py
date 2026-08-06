python
import random
import statistics
import pytest

from src_0003 import task_func

LETTERS = ['A', 'B', 'C', 'D', 'E']

def test_task_func():
    random_dict = {k: [random.randint(0, 100) for _ in range(random.randint(1, 10))] for k in LETTERS}
    sorted_dict = dict(sorted(random_dict.items(), key=lambda item: statistics.mean(item[1]), reverse=True))
    assert task_func(LETTERS) == sorted_dict