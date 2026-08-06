python
import random
import statistics
import pytest

def task_func(LETTERS):
    random_dict = {k: [random.randint(0, 100) for _ in range(random.randint(1, 10))] for k in LETTERS}
    sorted_dict = dict(sorted(random_dict.items(), key=lambda item: statistics.mean(item[1]), reverse=True))
    return sorted_dict

def test_task_func():
    LETTERS = ['A', 'B', 'C', 'D', 'E']
    sorted_dict = task_func(LETTERS)
    assert sorted_dict['A'][0] >= sorted_dict['B'][0]
    assert sorted_dict['B'][0] >= sorted_dict['C'][0]
    assert sorted_dict['C'][0] >= sorted_dict['D'][0]
    assert sorted_dict['D'][0] >= sorted_dict['E'][0]