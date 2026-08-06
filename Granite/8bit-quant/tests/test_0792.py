import random
from collections import Counter

from src_0792 import task_func

ELEMENTS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

def test_task_func_with_empty_list():
    assert task_func([]) == Counter()

def test_task_func_with_non_empty_list():
    l = list(ELEMENTS)
    random.shuffle(l)
    expected_counter = Counter(l[:30])
    keys = list(expected_counter.keys())
    expected_counter = Counter({k: expected_counter[k] for k in keys[3:] + keys[:3]})
    assert task_func(l) == expected_counter