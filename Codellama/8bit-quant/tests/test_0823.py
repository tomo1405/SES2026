import random

import pytest
from src_0823 import task_func


def test_task_func_length_positive():
    with pytest.raises(ValueError):
        task_func(0, 0)

def test_task_func_num_digits_negative():
    with pytest.raises(ValueError):
        task_func(10, -1)

def test_task_func_num_digits_greater_than_length():
    with pytest.raises(ValueError):
        task_func(10, 11)

def test_task_func_length_and_num_digits_valid():
    password = task_func(10, 2)
    assert len(password) == 10
    assert password.count(random.choice(LETTERS)) == 8
    assert password.count(random.choice(DIGITS)) == 2