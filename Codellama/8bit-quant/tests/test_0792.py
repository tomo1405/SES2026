import random
from typing import Counter

from src_0792 import task_func


def test_task_func_empty_list():
    assert task_func([]) == Counter()

def test_task_func_non_empty_list():
    l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    random.shuffle(l)
    l_cycled = cycle(l)
    counter = Counter(next(l_cycled) for _ in range(30))
    keys = list(counter.keys())
    counter = Counter({k: counter[k] for k in keys[3:] + keys[:3]})
    assert task_func(l) == counter