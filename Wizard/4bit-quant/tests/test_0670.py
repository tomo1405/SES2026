python
import itertools
import math
import pytest

from src_0670 import task_func

@pytest.mark.parametrize("x, expected", [
    ({'a': 0, 'b': 1, 'c': 2}, ('a', 'b')),
    ({'a': 0, 'b': 2, 'c': 1}, ('a', 'c')),
    ({'a': 1, 'b': 0, 'c': 2}, ('b', 'c')),
    ({'a': 1, 'b': 2, 'c': 0}, ('b', 'a')),
    ({'a': 2, 'b': 0, 'c': 1}, ('c', 'a')),
    ({'a': 2, 'b': 1, 'c': 0}, ('c', 'b')),
])
def test_task_func(x, expected):
    assert task_func(x) == expected