import itertools
import math

import pytest
from src_0670 import task_func


def test_task_func():
    x = {1: 1, 2: 2, 3: 3}
    pairs = list(itertools.combinations(x.keys(), 2))
    max_pair = max(pairs, key=lambda pair: math.cos(x[pair[0]]) + math.cos(x[pair[1]]))
    assert task_func(x) == max_pair

def test_task_func_empty_input():
    x = {}
    assert task_func(x) == None

def test_task_func_invalid_input():
    x = "invalid input"
    with pytest.raises(TypeError):
        task_func(x)