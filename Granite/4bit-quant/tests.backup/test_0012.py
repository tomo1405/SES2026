import numpy as np
import itertools
import random
from src_0012 import task_func

def test_task_func():
    T1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    p25, p50, p75 = task_func(T1)
    assert isinstance(p25, float) and isinstance(p50, float) and isinstance(p75, float)
    assert 0 <= p25 <= 100 and 0 <= p50 <= 100 and 0 <= p75 <= 100
    assert p25 < p50 < p75

def test_task_func_with_max_value():
    T1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    max_value = 50
    p25, p50, p75 = task_func(T1, max_value)
    assert isinstance(p25, float) and isinstance(p50, float) and isinstance(p75, float)
    assert 0 <= p25 <= max_value and 0 <= p50 <= max_value and 0 <= p75 <= max_value
    assert p25 < p50 < p75

def test_task_func_with_empty_list():
    T1 = [[]]
    p25, p50, p75 = task_func(T1)
    assert p25 is None and p50 is None and p75 is None