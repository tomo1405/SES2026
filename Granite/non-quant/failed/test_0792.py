import pytest
from collections import Counter
import random
from itertools import cycle
from src_0792 import task_func

ELEMENTS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

def test_task_func_with_empty_list():
    assert task_func([]) == Counter()

def test_task_func_with_non_empty_list():
    l = list(ELEMENTS)
    random.shuffle(l)
    expected_counter = Counter(l[:30])
    actual_counter = task_func(l)
    expected_keys = list(expected_counter.keys())
    actual_keys = list(actual_counter.keys())
    expected_counter = Counter({k: expected_counter[k] for k in expected_keys[3:] + expected_keys[:3]})
    actual_counter = Counter({k: actual_counter[k] for k in actual_keys[3:] + actual_keys[:3]})
    assert actual_counter == expected_counter