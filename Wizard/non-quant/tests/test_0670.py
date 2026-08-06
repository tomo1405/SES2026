python
import itertools
import math
import pytest

from src_0670 import task_func

def test_task_func():
    x = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}
    pairs = list(itertools.combinations(x.keys(), 2))
    max_pair = max(pairs, key=lambda pair: math.cos(x[pair[0]]) + math.cos(x[pair[1]]))
    assert task_func(x) == max_pair