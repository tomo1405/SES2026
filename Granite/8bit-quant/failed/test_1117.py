import pytest
from src_1117 import task_func
import random
import statistics

# Constants
AGE_RANGE = (22, 60)

def test_task_func():
    dict1 = {'EMP$$': 5, 'ENG$$': 3}
    mean_age, median_age, mode_age = task_func(dict1)
    assert mean_age > AGE_RANGE[0] and mean_age < AGE_RANGE[1]
    assert median_age > AGE_RANGE[0] and median_age < AGE_RANGE[1]
    assert mode_age == []

def test_task_func_no_employees():
    dict1 = {'DEV$$': 0}
    mean_age, median_age, mode_age = task_func(dict1)
    assert mean_age == 0
    assert median_age == 0
    assert mode_age == []

def test_task_func_invalid_input():
    with pytest.raises(TypeError):
        task_func('invalid input')