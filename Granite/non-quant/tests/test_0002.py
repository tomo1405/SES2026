import pytest
from src_0002 import task_func
import collections
import random
import string

def test_task_func_valid_input():
    assert task_func(100) == collections.Counter(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=100))

def test_task_func_zero_length():
    with pytest.raises(ValueError):
        task_func(0)

def test_task_func_negative_length():
    with pytest.raises(ValueError):
        task_func(-1)