import pytest
from src_0395 import task_func
import collections
import string
import random

def test_task_func():
    length = 10
    seed = 0
    random.seed(seed)
    random_string = ''.join(random.choice(string.ascii_letters) for _ in range(length))
    char_freq = collections.Counter(random_string)
    expected_output = dict(char_freq)
    actual_output = task_func(length, seed)
    assert actual_output == expected_output

def test_task_func_with_negative_length():
    with pytest.raises(ValueError):
        task_func(-10, 0)

def test_task_func_with_non_integer_length():
    with pytest.raises(TypeError):
        task_func('abc', 0)

def test_task_func_with_non_integer_seed():
    with pytest.raises(TypeError):
        task_func(10, 'abc')