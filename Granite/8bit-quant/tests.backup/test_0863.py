import random
import string
from collections import defaultdict
from src_0863 import task_func
import pytest

def test_task_func_with_seed():
    n = 10
    seed = 42
    random.seed(seed)
    expected_result = defaultdict(list)
    for _ in range(n):
        letter = random.choice(string.ascii_lowercase)
        expected_result[letter].append(letter)
    actual_result = task_func(n, seed)
    assert actual_result == expected_result

def test_task_func_without_seed():
    n = 10
    expected_result = defaultdict(list)
    for _ in range(n):
        letter = random.choice(string.ascii_lowercase)
        expected_result[letter].append(letter)
    actual_result = task_func(n)
    assert actual_result == expected_result

def test_task_func_with_zero_n():
    n = 0
    expected_result = defaultdict(list)
    actual_result = task_func(n)
    assert actual_result == expected_result

def test_task_func_with_negative_n():
    n = -10
    with pytest.raises(ValueError):
        task_func(n)