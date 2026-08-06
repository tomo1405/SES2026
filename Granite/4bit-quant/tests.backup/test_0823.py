import pytest
from src_0823 import task_func
import random
import string

LETTERS = string.ascii_letters
DIGITS = string.digits

def test_task_func():
    random.seed(42)
    password = task_func(10, 3)
    assert len(password) == 10
    assert all(c in DIGITS for c in password)

def test_task_func_invalid_length():
    with pytest.raises(ValueError):
        task_func(-1, 3)

def test_task_func_invalid_num_digits():
    with pytest.raises(ValueError):
        task_func(10, -1)
    with pytest.raises(ValueError):
        task_func(10, 11)