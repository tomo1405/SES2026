import pytest
from src_1117 import task_func

def test_task_func():
    dict1 = {'EMP$$': 5, 'DEV$$': 3, 'TEST$$': 2}
    mean_age, median_age, mode_age = task_func(dict1)
    assert mean_age > 22 and mean_age < 60
    assert median_age > 22 and median_age < 60
    assert len(mode_age) == 1 and mode_age[0] > 22 and mode_age[0] < 60

def test_no_employees():
    dict1 = {'NOT_EMP$$': 5, 'DEV$$': 3, 'TEST$$': 2}
    mean_age, median_age, mode_age = task_func(dict1)
    assert mean_age == 0 and median_age == 0 and mode_age == []