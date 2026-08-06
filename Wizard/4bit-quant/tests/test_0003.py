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
    assert sorted_dict['A'] == sorted(random_dict['A'], reverse=True)
    assert sorted_dict['B'] == sorted(random_dict['B'], reverse=True)
    assert sorted_dict['C'] == sorted(random_dict['C'], reverse=True)
    assert sorted_dict['D'] == sorted(random_dict['D'], reverse=True)
    assert sorted_dict['E'] == sorted(random_dict['E'], reverse=True)