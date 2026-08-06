from typing import Counter

import pytest
from src_0859 import task_func


def test_task_func():
    n = 10
    seed = 1234
    expected_result = Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1, 'e': 1})
    assert task_func(n, seed) == expected_result

def test_task_func_no_seed():
    n = 10
    expected_result = Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1, 'e': 1})
    assert task_func(n) == expected_result

def test_task_func_invalid_input():
    n = -1
    seed = 1234
    with pytest.raises(ValueError):
        task_func(n, seed)